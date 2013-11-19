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
    ACCESS_PUBLICSTATIC = 9
    CODE_INDEX = 7
    MAX_STACK = 512
    
    # Class fields
    codeGen = CodeGenerator()
    constantPool = ConstantPoolIndexer()
    fieldList = ArrayList()
    methodList = ArrayList()
    code = ArrayList()
    
    # Index's
    printIntIndex = 0
    printStrIndex = 0
    
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
        
    @vis.when(mjc_IntegerLiteral)
    def visit(self, node):
        self.printStrIndex = 0
        self.printIntIndex = self.constantPool.getInteger(node.i)
        
    @vis.when(mjc_StringLiteral)
    def visit(self, node):
        self.printIntIndex = 0
        self.printStrIndex = self.constantPool.getString(node.s)
    
    @vis.when(mjc_True)
    def visit(self, node):
        self.printIntIndex = 0
        self.printStrIndex = self.constantPool.getString("true")
    
    @vis.when(mjc_False)
    def visit(self, node):
        self.printIntIndex = 0
        self.printStrIndex = self.constantPool.getString("false")
        
    @vis.when(mjc_Null)
    def visit(self, node):
        self.printIntIndex = 0
        self.printStrIndex = self.constantPool.getString("null") 
        
    @vis.when(mjc_Print)
    def visit(self, node):
        # handle EXP to print
        node.e.accept(self)
        # getstatic 'out'
        self.code.add(0xb2)
        self.code.add(0x00)
        self.code.add(0x0d)
        if self.printIntIndex != 0:
            # ldc & index
            self.code.add(0x12)
            self.code.add(self.printIntIndex)
            # invokevirtual 'println'
            self.code.add(0xb6)
            self.code.add(0x00)
            self.code.add(0x13)
        elif self.printStrIndex != 0:
            # ldc & index
            self.code.add(0x12)
            self.code.add(self.printStrIndex)
            # invokevirtual 'println'
            self.code.add(0xb6)
            self.code.add(0x00)
            self.code.add(0x19)
        
    @vis.when(mjc_MethodDeclSimple)
    def visit(self, node):
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
        
    @vis.when(mjc_ClassDeclSimple)
    def visit(self,node):
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
