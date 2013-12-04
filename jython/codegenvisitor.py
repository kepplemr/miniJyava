'''
Created on Nov 14, 2013

@author:      michael
@description: Visitor class used to generate MiniJava bytecode
'''
from util import *
import java.util.Hashtable as Hashtable

class CodeGenVisitor(VisitorAdaptor):
    # Constants
    ACCESS_PUBLIC = 1
    ACCESS_PUBLICSTATIC = 9
    CODE_INDEX = 7
    MAX_STACK = 512
    
    # Class fields/index's
    classSym = Symbol.symbol("")
    methodSym = Symbol.symbol("")
    symTab = Table.getInstance()
    codeGener = CodeGenerator()
    constantPool = ConstantPoolIndexer()
    fieldList = ArrayList()
    methodList = ArrayList()
    code = ArrayList()
    formalList = ""
    expList = ""
    expType = 0
    expIndex = 0
    
    """ Required generic method to initialize dynamic dispatcher """        
    @vis.on('node')
    def visit(self, node):
        pass

    """ Adds fieldRef to constant pool and class fieldList """
    @vis.when(mjc_VarDecl)
    def visit(self, node):
        name = typeConvert(node.i.toString())
        type = typeConvert(node.t.toString())
        nameIndex = self.constantPool.getUtf8(name)
        typeIndex = self.constantPool.getUtf8(type)
        self.constantPool.getFieldInfo(self.classSym.toString(), name, type)
        field = FieldInfo(self.ACCESS_PUBLIC, nameIndex, typeIndex)
        self.fieldList.add(field)
        
    """ EXP visitor methods """
    @vis.when(mjc_Add)
    def visit(self, node):
        arithmeticExpression(self, node, "Add")
    @vis.when(mjc_Sub)
    def visit(self, node):
        arithmeticExpression(self, node, "Sub")
    @vis.when(mjc_Mult)
    def visit(self, node):
        arithmeticExpression(self, node, "Mul")
    @vis.when(mjc_Div)
    def visit(self, node):
        arithmeticExpression(self, node, "Div")
    @vis.when(mjc_GT)
    def visit(self, node):
        comparisonExpression(self, node, "GT")
    @vis.when(mjc_LT)
    def visit(self, node):
        comparisonExpression(self, node, "LT")
    @vis.when(mjc_GTEQ)
    def visit(self, node):
        comparisonExpression(self, node, "GTE")
    @vis.when(mjc_LTEQ)
    def visit(self, node):
        comparisonExpression(self, node, "LTE")
    @vis.when(mjc_DoubleEqual)
    def visit(self, node):
        comparisonExpression(self, node, "EQ")
    @vis.when(mjc_NotEqual)
    def visit(self, node):
        comparisonExpression(self, node, "NE")
    @vis.when(mjc_IntegerLiteral)
    def visit(self, node):
        self.expType = EXP_INTINDEX
        self.expIndex = self.constantPool.getInteger(node.i)
    @vis.when(mjc_StringLiteral)
    def visit(self, node):
        self.expType = EXP_STRINDEX
        self.expIndex = self.constantPool.getString(node.s)
    @vis.when(mjc_True)
    def visit(self, node):
        self.expType = EXP_IMMBOOL
        self.expIndex = 1
        self.code.add(0x10)
        self.code.add(0x01)
    @vis.when(mjc_False)
    def visit(self, node):
        self.expType = EXP_IMMBOOL
        self.expIndex = 0
        self.code.add(0x10)
        self.code.add(0x00)
    @vis.when(mjc_Null)
    def visit(self, node):
        self.expType = EXP_STRINDEX
        self.expIndex = self.constantPool.getString("null")
    @vis.when(mjc_This)
    def visit(self, node):
        self.expType = EXP_STRINDEX
        self.expIndex = self.constantPool.getString(self.classSym.toString())
    @vis.when(mjc_Identifier)
    def visit(self, node):
        self.expIndex = getLocation(self, self.classSym, self.methodSym, node.s)
        idType = getType(self, self.classSym, self.methodSym, node.s)
        setType(self, idType)        
    @vis.when(mjc_IdentifierExp)
    def visit(self, node):
        self.expIndex = getLocation(self, self.classSym, self.methodSym, node.s)
        idType = getType(self, self.classSym, self.methodSym, node.s)
        setType(self, idType)
    @vis.when(mjc_NewArray)
    def visit(self, node):
        node.e.accept(self)
        self.expType = EXP_NEWARRAY
    @vis.when(mjc_ArrayLookup)
    def visit(self, node):
        # find location of array
        node.e1.accept(self)
        arrayType = self.expType
        # push arrayRef to stack
        pushToStack(self, EXP_LOCOBJECT, self.expIndex, None)
        node.e2.accept(self)
        # push arrayIndex to stack
        pushToStack(self, self.expType, self.expIndex, None)
        # push found arrayVal to stack
        pushToStack(self, arrayType, self.expIndex, None)
    @vis.when(mjc_NewObject)
    def visit(self, node):
        className = typeConvert(node.i.toString())
        classIndex = self.constantPool.getClass(className)
        initRef = self.constantPool.getMethodInfo(className, "<init>", "()V")
        # new <class>
        self.code.add(0xbb)
        self.code.add(0x00)
        self.code.add(classIndex)
        # dup
        self.code.add(0x59)
        # invokespecial
        self.code.add(0xb7)
        self.code.add(0x00)
        self.code.add(initRef)
        self.expType = EXP_OBJECT
    @vis.when(mjc_CallExpression)
    def visit(self, node):
        objLocation = getLocation(self, self.classSym, self.methodSym, typeConvert(node.e.toString()))
        getCall(self, node, objLocation)        
    @vis.when(mjc_ExpList)
    def visit(self, node):
        self.expList = "("
        for x in range (0, node.size()):
            node.elementAt(x).accept(self)
            if self.expType == EXP_STRARRAY:
                self.expType = EXP_LOCOBJECT
                self.expList += "[Ljava/lang/String;"
            elif self.expType == EXP_INTARRAY:
                self.expType = EXP_LOCOBJECT
                self.expList += "[I"
            elif self.expType == EXP_INTINDEX:
                self.expList += typeConvert(node.elementAt(x).toString()) 
            elif (self.expType == EXP_LOCINTIND or self.expType == EXP_LOCSTRIND
                  or self.expType == EXP_LOCBOOL):
                var = typeConvert(node.elementAt(x).toString())
                type = getType(self, self.classSym, self.methodSym, var)
                self.expList += type
            elif self.expType == EXP_LOCOBJECT:
                self.expList += getObjType(self, self.classSym, self.methodSym, node.elementAt(x).s)
            elif (isinstance(node.elementAt(x), mjc_This)):
                self.expList += ("L" + self.classSym.toString() + ";")
                self.expType = EXP_LOCOBJECT;
                self.expIndex = 0
            else:
                self.expList += typeConvert(node.elementAt(x).toString())                
            pushToStack(self, self.expType, self.expIndex, None)
        self.expList += ")"
    @vis.when(mjc_Not)
    def visit(self, node):
        node.e.accept(self)
        if (isinstance(node.e, mjc_IdentifierExp)):
            pushToStack(self, self.expType, self.expIndex, None)
        # ifeq <branch past 'push 1'>
        self.code.add(0x99)
        self.code.add(0x00)
        self.code.add(0x08)
        # bipush 0
        self.code.add(0x10)
        self.code.add(0x00)
        # goto +3
        self.code.add(0xa7)
        self.code.add(0x00)
        self.code.add(0x05)
        # bipush 1
        self.code.add(0x10)
        self.code.add(0x01)
    @vis.when(mjc_And)
    def visit(self, node):
        node.e1.accept(self)
        if (isinstance(node.e1, mjc_IdentifierExp)):
            pushToStack(self, self.expType, self.expIndex, None)
        node.e2.accept(self)
        if (isinstance(node.e2, mjc_IdentifierExp)):
            pushToStack(self, self.expType, self.expIndex, None)
        self.code.add(0x7e)
    @vis.when(mjc_Or)
    def visit(self, node):
        print("Or!")
    
    
    
    """ Statement visitor methods """
    @vis.when(mjc_If)
    def visit(self, node):
        node.e.accept(self)
        if (isinstance(node.e, mjc_IdentifierExp)):
            pushToStack(self, self.expType, self.expIndex, None)
        codeCopy = ArrayList(self.code)
        self.code.clear()
        node.s1.accept(self)
        # ifeq <branch past true statements>
        codeCopy.add(0x99)
        codeCopy.add(0x00)
        codeCopy.add(self.code.size()+6)
        codeCopy.addAll(self.code)
        self.code.clear()
        node.s2.accept(self)
        # goto -> after else
        codeCopy.add(0xa7)
        codeCopy.add(0x00)
        codeCopy.add(self.code.size()+3)
        codeCopy.addAll(self.code)
        self.code = ArrayList(codeCopy)
    @vis.when(mjc_CallStatement)
    def visit(self, node):
        objLocation = getLocation(self, self.classSym, self.methodSym, typeConvert(node.e.toString()))
        getCall(self, node, objLocation)
    @vis.when(mjc_Block)
    def visit(self, node):
        for x in range(0, node.sl.size()):
            node.sl.elementAt(x).accept(self)
    @vis.when(mjc_Print)
    def visit(self, node):
        # getstatic 'out'
        self.code.add(0xb2)
        self.code.add(0x00)
        self.code.add(0x0d)
        # handle EXP to print
        node.e.accept(self)
        if self.expType == EXP_FIELD_INT or self.expType == EXP_FIELD_OBJECT:
            printPush(self, 0x13)
        elif self.expType == EXP_FIELD_STRING:
            printPush(self, 0x19)
        elif (self.expType == EXP_INTINDEX or self.expType == EXP_LOCINTIND 
            or self.expType == EXP_LOCOBJECT):
            printPush(self, 0x13)
        elif (self.expType == EXP_LOCBOOL or self.expType == EXP_BOOLVAL or
              self.expType == EXP_FIELD_BOOL):
            printPush(self, 0x16)
        elif self.expType == EXP_IMMBOOL:
            printImm(self, 0x16)
        elif self.expType == EXP_IMMINTVAL:
            printImm(self, 0x13)
        elif (self.expType == EXP_STRINDEX or self.expType == EXP_LOCSTRIND
              or self.expType == EXP_IMMSTRREF):
            printPush(self, 0x19)
    @vis.when(mjc_Assign)
    def visit(self, node):
        typeString = getType(self, self.classSym, self.methodSym, typeConvert(node.i.toString()))
        if typeString[:3] == "<f>":
            loadInstance(self)
        node.e.accept(self)
        pushToStack(self, self.expType, self.expIndex, typeString)
        location = getLocation(self, self.classSym, self.methodSym, typeConvert(node.i.toString()))
        # if != NEWARRAY?
        if typeString[:3] == "<f>" or typeString == "Z":
            node.i.accept(self)
        popToLocal(self, self.expType, location)        
    @vis.when(mjc_ArrayAssign)
    def visit(self, node):
        location = getLocation(self, self.classSym, self.methodSym, typeConvert(node.i.toString()))
        methFieldType = getType(self, self.classSym, self.methodSym, typeConvert(node.i.toString()))
        pushToStack(self, EXP_LOCOBJECT, location, None)
        node.e1.accept(self)
        pushToStack(self, self.expType, self.expIndex, None)
        node.e2.accept(self)
        pushToStack(self, self.expType, self.expIndex, None)
        popToLocal(self, EXP_INTARRAY, None) if methFieldType == "[I" else popToLocal(self, EXP_STRARRAY, None)
        
    """ Formal/FormalList visitor methods """
    @vis.when(mjc_Formal)
    def visit(self, node):
        if isObject(node.t.toString()):
            self.formalList += getObjType(self, self.classSym, self.methodSym, node.i.s)
        else:
            self.formalList += typeConvert(node.t.toString())    
    @vis.when(mjc_FormalList)
    def visit(self, node):
        self.formalList = "("
        for x in range (0, node.size()):
            node.elementAt(x).accept(self)
        self.formalList += ")"
    
    """ Method visitor methods """
    @vis.when(mjc_MethodVoidType)
    def visit(self, node):
        self.formalList += "V"
    @vis.when(mjc_MethodReturnType)
    def visit(self, node):
        if isObject(node.t.toString()):
            self.formalList += ("L" + typeConvert(node.toString()) + ";")
        else:
            self.formalList += typeConvert(node.toString())
    @vis.when(mjc_MethodDeclSimple)
    def visit(self, node):
        getMethod(self, node, "simple")
    @vis.when(mjc_MethodDeclStatic)
    def visit(self, node):
        getMethod(self, node, "static")
    
    """ Class visitor methods """   
    @vis.when(mjc_ClassDeclSimple)
    def visit(self,node):
        getClass(self, node, "simple") 
    @vis.when(mjc_ClassDeclExtends)
    def visit(self, node):
        getClass(self, node, "extends")
    
    """ Root node of AST tree - begin code generation here """
    @vis.when(mjc_ClassDeclList)
    def visit(self, node):
        # Constant pools are not shared between multiple classes in one file.
        for x in range(0, node.size()):
            self.constantPool.clearConstantPool()
            self.constantPool.createPrintLineEntries()
            self.constantPool.getString("--- Inside Class Constr: " + repr(x) + " ---")
            node.elementAt(x).accept(self)
        self.codeGener.writeFiles()