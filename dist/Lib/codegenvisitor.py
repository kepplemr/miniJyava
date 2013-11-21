'''
Created on Nov 14, 2013

@author:      michael
@description: Visitor class used to generate MiniJava bytecode
'''
from util import *

class CodeGenVisitor(VisitorAdaptor):
    # Constants
    ACCESS_PUBLIC = 1
    EXP_INTINDEX = 2
    EXP_STRINDEX = 3
    EXP_LOCINTIND = 4
    EXP_LOCSTRIND = 5
    EXP_IMMINTVAL = 6
    EXP_BOOLVAL = 7
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
        self.expType = self.EXP_INTINDEX
        self.expIndex = self.constantPool.getInteger(node.i)
    @vis.when(mjc_StringLiteral)
    def visit(self, node):
        self.expType = self.EXP_STRINDEX
        self.expIndex = self.constantPool.getString(node.s)
    @vis.when(mjc_True)
    def visit(self, node):
        self.expType = self.EXP_BOOLVAL
        self.expIndex = 0
        # bipush 1
        self.code.add(0x10)
        self.code.add(0x01)
    @vis.when(mjc_False)
    def visit(self, node):
        self.expType = self.EXP_BOOLVAL
        self.expIndex = 0
        #bipush 0
        self.code.add(0x10)
        self.code.add(0x00)
    @vis.when(mjc_Null)
    def visit(self, node):
        self.expType = self.EXP_STRINDEX
        self.expIndex = self.constantPool.getString("null") 
    @vis.when(mjc_IdentifierExp)
    def visit(self, node):
        currSym = Symbol.symbol(mjc_Identifier(node.s).toString())
        methFieldEntry = self.symTab.getMethodLocal(self.classSym, self.methodSym, currSym)
        methFieldType = typeConvert(methFieldEntry.getType().toString())
        self.expIndex = methFieldEntry.getLocation()
        if methFieldType == "I":
            self.expType = self.EXP_LOCINTIND
        elif methFieldType == "Ljava/lang/String;":
            self.expType = self.EXP_LOCSTRIND
    
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
        if self.expType == self.EXP_INTINDEX:
            # ldc & index
            self.code.add(0x12)
            self.code.add(self.expIndex)
            # invokevirtual 'println(CP_IntIndex)'
            self.code.add(0xb6)
            self.code.add(0x00)
            self.code.add(0x13)
        elif self.expType == self.EXP_STRINDEX:
            # ldc & index
            self.code.add(0x12)
            self.code.add(self.expIndex)
            # invokevirtual 'println(CP_StrIndex)'
            self.code.add(0xb6)
            self.code.add(0x00)
            self.code.add(0x19)
        elif self.expType == self.EXP_IMMINTVAL:
            # invokevirtual 'println(42)'
            self.code.add(0xb6)
            self.code.add(0x00)
            self.code.add(0x13)
        elif self.expType == self.EXP_LOCINTIND:
            # iload <local>
            self.code.add(0x15)
            self.code.add(self.expIndex)
            # invokevirtual 'println(int i)
            self.code.add(0xb6)
            self.code.add(0x00)
            self.code.add(0x13)
        elif self.expType == self.EXP_LOCSTRIND:
            # aload <local>
            self.code.add(0x19)
            self.code.add(self.expIndex)
            # invokevirtual 'println(String str)'
            self.code.add(0xb6)
            self.code.add(0x00)
            self.code.add(0x19)
        elif self.expType == self.EXP_BOOLVAL:
            # invokevirtual 'println(boolean)'
            self.code.add(0xb6)
            self.code.add(0x00)
            self.code.add(0x16)
            
    @vis.when(mjc_Assign)
    def visit(self, node):
        currSym = Symbol.symbol(node.i.toString())
        methFieldEntry = self.symTab.getMethodLocal(self.classSym, self.methodSym, currSym)
        methFieldType = typeConvert(methFieldEntry.getType().toString())
        location = methFieldEntry.getLocation()
        node.e.accept(self)
        # calculate value of assignment expression
        self.code.add(0x12)
        self.code.add(self.expIndex)
        if methFieldType == "I":
            # istore <location>
            self.code.add(0x36)
            self.code.add(location)
        elif methFieldType == "Ljava/lang/String;":
            # astore <location>
            self.code.add(0x3a)
            self.code.add(location)
    
    """ Method visitor methods """
    @vis.when(mjc_MethodDeclSimple)
    def visit(self, node):
        # Set method symbol marker
        self.methodSym = Symbol.symbol(node.i.toString())
        self.code = ArrayList()
        type = "("
        for x in range (0, node.fl.size()):
            type += typeConvert(node.fl.elementAt(x).t.toString())
        type += ")"
        type += typeConvert(node.t.toString())
        nameIndex = self.constantPool.getUtf8(typeConvert(node.i.toString()))
        typeIndex = self.constantPool.getUtf8(type)
        maxLocals = node.fl.size() + node.vl.size()
        # Handle method statements
        for x in range(0, node.sl.size()):
            node.sl.elementAt(x).accept(self)
        # empty return opcode
        self.code.add(0xb1)
        method = MethodInfo(self.ACCESS_PUBLIC, nameIndex, typeIndex, self.CODE_INDEX, self.code.size()+12, self.MAX_STACK, maxLocals, self.code)
        self.methodList.add(method)
         
    @vis.when(mjc_MethodDeclStatic)
    def visit(self, node):
        # Set method symbol marker
        self.methodSym = Symbol.symbol(node.i.toString())
        self.code = ArrayList()
        type = "("
        for x in range (0, node.fl.size()):
            type += typeConvert(node.fl.elementAt(x).t.toString())
        type += ")"
        type += typeConvert(node.t.toString())
        nameIndex = self.constantPool.getUtf8(typeConvert(node.i.toString()))
        typeIndex = self.constantPool.getUtf8(type)
        maxLocals = node.fl.size() + node.vl.size()
        # Handle method statements
        for x in range(0, node.sl.size()):
            node.sl.elementAt(x).accept(self)
        # empty return opcode
        self.code.add(0xb1)
        method = MethodInfo(self.ACCESS_PUBLICSTATIC, nameIndex, typeIndex, self.CODE_INDEX, self.code.size()+12, self.MAX_STACK, maxLocals, self.code)
        self.methodList.add(method)
    
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
        self.constantPool.clearConstantPool()
        self.constantPool.createPrintLineEntries()
        for x in range(0, node.size()):
            node.elementAt(x).accept(self)
        self.codeGener.writeFiles()