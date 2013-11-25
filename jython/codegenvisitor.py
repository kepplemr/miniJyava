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
        self.expIndex = getLocation(self, self.classSym, self.methodSym, node.s)
        methFieldType = getFieldType(self, self.classSym, self.methodSym, node.s)
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
        
    """ Call methods """
    @vis.when(mjc_CallExpression)
    def visit(self, node):
        # Find local location of invoked object and load it
        objLocation = getLocation(self, self.classSym, self.methodSym, node.e.s)
        # aload <object>
        self.code.add(0x19)
        self.code.add(objLocation)
        # Create method type based off ExpList arguments and push them on stack
        node.el.accept(self);
        methRef = getMethodReference(self, node)        
        # invokevirtual <method>
        self.code.add(0xb6)
        self.code.add(0x00)
        self.code.add(methRef)
        # $$$$$$$$$$$$
        self.expType = EXP_IMMINTVAL  
    @vis.when(mjc_CallStatement)
    def visit(self, node):
        # Find local location of invoked object and load it
        objLocation = getLocation(self, self.classSym, self.methodSym, node.e.s)
        node.el.accept(self);
        # aload <object>
        self.code.add(0x19)
        self.code.add(objLocation)
        # Create method type based off ExpList arguments and push them on stack
        node.el.accept(self);
        methRef = getMethodReference(self, node)        
        # invokevirtual <method>
        self.code.add(0xb6)
        self.code.add(0x00)
        self.code.add(methRef)
        # $$$$$$$$$$$$
        self.expType = EXP_IMMINTVAL
        
    @vis.when(mjc_ExpList)
    def visit(self, node):
        self.expList = "("
        for x in range (0, node.size()):
            node.elementAt(x).accept(self)
            # int
            if self.expType == 2:
                self.code.add(0x10)
                self.code.add(0x01)
            self.expList += typeConvert(node.elementAt(x).toString())
        self.expList += ")"
    
    @vis.when(mjc_Formal)
    def visit(self, node):
        print("Formal!")
    @vis.when(mjc_FormalList)
    def visit(self, node):
        print("FormalList!")
    
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
        location = getLocation(self, self.classSym, self.methodSym, typeConvert(node.i.toString()))
        methFieldType = getFieldType(self, self.classSym, self.methodSym, typeConvert(node.i.toString()))
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
            if methFieldType == "[I":
                newIntArray(self, self.expIndex, location)
            else:
                newStringArray(self, self.expIndex, location)
    @vis.when(mjc_ArrayAssign)
    def visit(self, node):
        location = getLocation(self, self.classSym, self.methodSym, typeConvert(node.i.toString()))
        methFieldType = getFieldType(self, self.classSym, self.methodSym, typeConvert(node.i.toString()))
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