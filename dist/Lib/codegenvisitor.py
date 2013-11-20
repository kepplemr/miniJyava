'''
Created on Nov 14, 2013

@author:      michael
@description: Visitor class used to generate MiniJava bytecode
'''
import struct
import sys
import dispatch as vis
from os.path import dirname, realpath, sep, pardir
temp = sep + pardir + sep + pardir + sep
sys.path.append(dirname(realpath(__file__)) + temp + "classes")
import java.util.ArrayList as ArrayList
import util
from javacode import *
from javacode.symbol import *
from javacode.syntaxtree import *
from javacode.classwriter import *
from javacode.classwriter.constantpool import *

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
    codeGen = CodeGenerator()
    constantPool = ConstantPoolIndexer()
    fieldList = ArrayList()
    methodList = ArrayList()
    code = ArrayList()
    
    # Index's
    expType = 0
    expIndex = 0
    
    """ Add default <init> constructor """
    def addInit(self):
        self.code = ArrayList()
        # aload_0
        self.code.add(0x2a)
        # invokespecial #1
        self.code.add(0xb7)
        self.code.add(0x00)
        self.code.add(0x06)
        # return
        self.code.add(0xb1)
        init = MethodInfo(0, 3, 4, 7, self.code.size()+12, 512, 512, self.code)
        self.methodList.add(init)

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
        self.expIndex = 0
        # push both EXP's to stack
        node.e1.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        node.e2.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        # iadd 
        self.code.add(0x60)  
        self.expType = self.EXP_IMMINTVAL
        
    @vis.when(mjc_Sub)
    def visit(self, node):
        self.expIndex = 0
        # push both EXP's to stack
        node.e1.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        node.e2.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        # isub 
        self.code.add(0x64)  
        self.expType = self.EXP_IMMINTVAL
        
    @vis.when(mjc_Mult)
    def visit(self, node):
        self.expIndex = 0
        # push both EXP's to stack
        node.e1.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        node.e2.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        # imul
        self.code.add(0x68)  
        self.expType = self.EXP_IMMINTVAL
        
    @vis.when(mjc_Div)
    def visit(self, node):
        self.expIndex = 0
        # push both EXP's to stack
        node.e1.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        node.e2.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        # idiv
        self.code.add(0x6c)  
        self.expType = self.EXP_IMMINTVAL
    
    @vis.when(mjc_GT)
    def visit(self, node):
        self.expIndex = 0
        # push both EXP's to stack
        node.e1.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        node.e2.accept(self)
        self.code.add(0x12)
        self.code.add(self.expIndex)
        # if_icmpgt -> (branch + 8)
        self.code.add(0xa3)
        self.code.add(0x00)
        self.code.add(0x08)
        # bipush 0
        self.code.add(0x10)
        self.code.add(0x00)
        # goto -> (branch + 5)
        self.code.add(0xa7)
        self.code.add(0x00)
        self.code.add(0x05)
        # bipush 1
        self.code.add(0x10)
        self.code.add(0x01)
        self.expType = self.EXP_BOOLVAL
        
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
        methFieldType = util.typeConvert(methFieldEntry.getType().toString())
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
        methFieldType = util.typeConvert(methFieldEntry.getType().toString())
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
            type += util.typeConvert(node.fl.elementAt(x).t.toString())
        type += ")"
        type += util.typeConvert(node.t.toString())
        nameIndex = self.constantPool.getUtf8(util.typeConvert(node.i.toString()))
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
            type += util.typeConvert(node.fl.elementAt(x).t.toString())
        type += ")"
        type += util.typeConvert(node.t.toString())
        nameIndex = self.constantPool.getUtf8(util.typeConvert(node.i.toString()))
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
        # Set class symbol marker
        self.classSym = Symbol.symbol(util.typeConvert(node.i.toString()))
        # Clear out global ArrayLists
        self.fieldList = ArrayList()
        self.methodList = ArrayList()
        self.constantPool.clearConstantPool()
        self.constantPool.createPrintLineEntries()
        self.addInit()
        # Handle class fields
        for x in range(0, node.vl.size()):
            node.vl.elementAt(x).accept(self)
        # Handle class methods
        for x in range(0, node.ml.size()):
            node.ml.elementAt(x).accept(self)
        classIndex = self.constantPool.getClass(node.i.s)
        self.codeGen.addClass(ClassFile(classIndex, 2, self.constantPool.getCPClone(), self.fieldList, self.methodList))
        
    @vis.when(mjc_ClassDeclExtends)
    def visit(self, node):
        # Set class symbol marker
        self.classSym = Symbol.symbol(util.typeConvert(node.i.toString()))
        # Clear out global ArrayLists
        self.fieldList = ArrayList()
        self.methodList = ArrayList()
        self.constantPool.clearConstantPool()
        self.constantPool.createPrintLineEntries()
        self.addInit()
        # Handle class fields
        for x in range(0, node.vl.size()):
            node.vl.elementAt(x).accept(self)
        # Handle class methods
        for x in range(0, node.ml.size()):
            node.ml.elementAt(x).accept(self)
        classIndex = self.constantPool.getClass(node.i.s)
        self.codeGen.addClass(ClassFile(classIndex, 2, self.constantPool.getCPClone(), self.fieldList, self.methodList))
    
    """ Root node of AST tree - begin code generation here """
    @vis.when(mjc_ClassDeclList)
    def visit(self, node):
        for x in range(0, node.size()):
            node.elementAt(x).accept(self)
        self.codeGen.writeFiles()