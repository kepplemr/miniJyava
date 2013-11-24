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
    
    # Symbol markers
    classSym = Symbol.symbol("")
    methodSym = Symbol.symbol("")
    
    # Class fields
    symTab = Table.getInstance()
    codeGener = CodeGenerator()
    constantPool = ConstantPoolIndexer()
    fieldList = ArrayList()
    methodList = ArrayList()
    code = ArrayList()
    expList = ""
    
    # Index's
    expType = 0
    expIndex = 0
    
    """ Generic method to initialize dynamic dispatcher """        
    @vis.on('node')
    def visit(self, node):
        pass

    @vis.when(mjc_VarDecl)
    def visit(self, node):
        print("Encountered VarDecl")
        nameIndex = self.constantPool.getUtf8(node.i.toString())
        typeIndex = self.constantPool.getUtf8(node.t.toString())
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
        self.expType = EXP_BOOLVAL
        self.expIndex = 0
        # bipush 1
        self.code.add(0x10)
        self.code.add(0x01)
    @vis.when(mjc_False)
    def visit(self, node):
        self.expType = EXP_BOOLVAL
        self.expIndex = 0
        #bipush 0
        self.code.add(0x10)
        self.code.add(0x00)
    @vis.when(mjc_Null)
    def visit(self, node):
        self.expType = EXP_STRINDEX
        self.expIndex = self.constantPool.getString("null") 
    @vis.when(mjc_IdentifierExp)
    def visit(self, node):
        currSym = Symbol.symbol(mjc_Identifier(node.s).toString())
        methFieldEntry = self.symTab.getMethodLocal(self.classSym, self.methodSym, currSym)
        methFieldType = typeConvert(methFieldEntry.getType().toString())
        self.expIndex = methFieldEntry.getLocation()
        if methFieldType == "I":
            self.expType = EXP_LOCINTIND
        elif methFieldType == "Ljava/lang/String;":
            self.expType = EXP_LOCSTRIND
        elif methFieldType == "[I":
            self.expType = EXP_INTARRAY
        elif methFieldType == "[Ljava/lang/String;":
            self.expType = EXP_STRARRAY
    @vis.when(mjc_NewArray)
    def visit(self, node):
        node.e.accept(self)
        self.expType = EXP_ARRAY
    @vis.when(mjc_ArrayLookup)
    def visit(self, node):
        # find location of array
        node.e1.accept(self)
        arrayType = self.expType
        # aload <arrayLocation>
        self.code.add(0x19)
        self.code.add(self.expIndex)
        node.e2.accept(self)
        # ldc <arrayIndex>
        self.code.add(0x12)
        self.code.add(self.expIndex)
        if arrayType == EXP_INTARRAY:
            # iaload
            self.code.add(0x2e)
            self.expType = EXP_IMMINTVAL
        elif arrayType == EXP_STRARRAY:
            # aaload
            self.code.add(0x32)
            self.expType = EXP_IMMSTRREF
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
        # Create expList
        node.el.accept(self);
        # Get some method info from object 
        currSym = Symbol.symbol(mjc_Identifier(node.e.s).toString())
        methFieldEntry = self.symTab.getMethodLocal(self.classSym, self.methodSym, currSym)
        # Discern class and method
        className = typeConvert(methFieldEntry.toString())
        methodName = node.i.toString()
        method = self.symTab.getMethod(Symbol.symbol(className), Symbol.symbol(methodName))
        self.expList += typeConvert(method.getResult())
        print("CE ExpList -> " + self.expList)
        
    @vis.when(mjc_CallStatement)
    def visit(self, node):
        node.el.accept(self);

        methodName = node.i.toString()
        currSym = Symbol.symbol(mjc_Identifier(node.e.s).toString())
        methFieldEntry = self.symTab.getMethodLocal(self.classSym, self.methodSym, currSym)
        location = methFieldEntry.getLocation()
        className = typeConvert(methFieldEntry.toString())
        print("Class -> " + className)
        print("Method -> " + typeConvert(methodName))
        method = self.symTab.getMethod(Symbol.symbol(className), Symbol.symbol(methodName))
        params = method.getParams()
        ret = method.result
        print(ret)
        ret = method.getName()
        print("HashTable size -> " + repr(params.size()))
        key = params.entrySet()
        iter = key.iterator()
        while iter.hasNext():
            print(typeConvert(str(iter.next())))      
        #type = "("
        #for x in range (0, mjc_Method.fl.size()):
        #    type += typeConvert(mjc_Method.fl.elementAt(x).t.toString())
        #type += ")"
        #type += typeConvert(mjc_Method.t.toString())
        # aload <object>
        self.code.add(0x19)
        self.code.add(location)
        self.expType = EXP_OBJECT
        
    @vis.when(mjc_ExpList)
    def visit(self, node):
        self.expList = "("
        for x in range (0, node.size()):
            print("ListEle -> " + node.elementAt(x).toString())
            self.expList += typeConvert(node.elementAt(x).toString())
        self.expList += ")"
    
    """ Statement visitor methods """
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
        if self.expType == EXP_INTINDEX:
            printCpIntIndex(self)
        elif self.expType == EXP_STRINDEX:
            printCpStrIndex(self)
        elif self.expType == EXP_IMMINTVAL:
            printImmIntVal(self)
        elif self.expType == EXP_LOCINTIND:
            printLocInt(self)
        elif self.expType == EXP_LOCSTRIND:
            printLocString(self)
        elif self.expType == EXP_BOOLVAL:
            printImmBoolVal(self)
    @vis.when(mjc_Assign)
    def visit(self, node):
        currSym = Symbol.symbol(node.i.toString())
        methFieldEntry = self.symTab.getMethodLocal(self.classSym, self.methodSym, currSym)
        location = methFieldEntry.getLocation()
        node.e.accept(self)
        if self.expType == EXP_INTINDEX:
            self.code.add(0x12)
            self.code.add(self.expIndex)
            # istore <location>
            self.code.add(0x36)
            self.code.add(location)
        elif self.expType == EXP_OBJECT:
            self.code.add(0x3a)
            self.code.add(location)
        elif self.expType == EXP_STRINDEX:
            self.code.add(0x12)
            self.code.add(self.expIndex)
            # astore <location>
            self.code.add(0x3a)
            self.code.add(location)
        elif self.expType == EXP_IMMINTVAL:
            # istore <location>
            self.code.add(0x36)
            self.code.add(location)
        elif self.expType == EXP_IMMSTRREF:
            # astore <location>
            self.code.add(0x3a)
            self.code.add(location)
        elif self.expType == EXP_ARRAY:
            methFieldType = typeConvert(methFieldEntry.getType().toString())
            if methFieldType == "[I":
                newIntArray(self, self.expIndex, location)
            else:
                newStringArray(self, self.expIndex, location)
    @vis.when(mjc_ArrayAssign)
    def visit(self, node):
        currSym = Symbol.symbol(node.i.toString())
        methFieldEntry = self.symTab.getMethodLocal(self.classSym, self.methodSym, currSym)
        methFieldType = typeConvert(methFieldEntry.getType().toString())
        location = methFieldEntry.getLocation()
        node.e1.accept(self)
        # retrieve array reference from local variable
        self.code.add(0x19)
        self.code.add(location)
        # ldc <cpIntArrayIndex>
        self.code.add(0x12)
        self.code.add(self.expIndex)
        # ldc <valToStore>
        node.e2.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        if methFieldType == "[I":
            # iastore
            self.code.add(0x4f)
        elif methFieldType == "[Ljava/lang/String;":
            # aastore
            self.code.add(0x53)
    
    """ Method visitor methods """
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
            self.constantPool.getString("--- Inside Class Constructor " + repr(x) + " ---")
            node.elementAt(x).accept(self)
        self.codeGener.writeFiles()