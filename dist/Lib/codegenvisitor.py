'''
Created on Nov 14, 2013

@author:      michael
@description: Visitor class used to generate MiniJava bytecode
'''
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
    CODE_INDEX = 7
    MAX_STACK = 512
    # Class fields
    codeGen = CodeGenerator()
    constantPool = ConstantPoolIndexer()
    fieldList = ArrayList()
    methodList = ArrayList()
    code = ArrayList()
    
    # Constructor
    def __init__(self):
        print("Created, yo")  
        
    @vis.on('node')
    def visit(self, node):
        """
        This is the generic method that initializes the
        dynamic dispatcher.
        """
    @vis.when(mjc_VarDecl)
    def visit(self, node):
        print("Encountered VarDecl")
        nameIndex = self.constantPool.getUtf8(node.i.toString())
        typeIndex = self.constantPool.getUtf8(node.t.toString())
        field = FieldInfo(self.ACCESS_PUBLIC, nameIndex, typeIndex)
        self.fieldList.add(field)
        
    @vis.when(mjc_Print)
    def visit(self, node):
        print("Print statement encountered")
        # b2 = getstatic opcode
        self.code.add(0xb2)
        # out -> CP(13)
        self.code.add(0x00)
        self.code.add(0x0d)
        # bipush opcode
        self.code.add(0x10)
        # byte immediate value to expand and push on stack
        self.code.add(0x30)
        # invokevirtual opcode
        self.code.add(0xb6)
        # cp index to println
        self.code.add(0x00)
        self.code.add(0x03)
        # empty return opcode
        self.code.add(0xb1)
        
    @vis.when(mjc_MethodDeclSimple)
    def visit(self, node):
        print("Encountered MethodDeclSimple")
        code = ArrayList()
        nameIndex = self.constantPool.getUtf8(node.i.toString())
        typeIndex = self.constantPool.getUtf8(node.t.toString())
        maxLocals = node.fl.size() + node.vl.size()
        for x in range(0, node.sl.size()):
            node.sl.elementAt(x).accept(self)
        # Code length obtained by braching down to all statements, etc. in method
         
    @vis.when(mjc_MethodDeclStatic)
    def visit(self, node):
        print("Encountered MethodDeclStatic")
        self.code = ArrayList()
        for x in range (0, node.fl.size()):
            print(node.fl.elementAt(x).t.toString())
            print(util.typeConvert(node.fl.elementAt(x).t.toString()))
        nameIndex = self.constantPool.getUtf8(node.i.toString())
        typeIndex = self.constantPool.getUtf8(node.t.toString())
        maxLocals = node.fl.size() + node.vl.size()
        for x in range(0, node.sl.size()):
            node.sl.elementAt(x).accept(self)
        method = MethodInfo(self.ACCESS_PUBLIC, nameIndex, typeIndex, self.CODE_INDEX, self.code.size()+12, self.MAX_STACK, maxLocals, self.code)
        self.methodList.add(method)
        
    @vis.when(mjc_ClassDeclSimple)
    def visit(self,node):
        print("Encountered classdecl")
        # Clear out global ArrayLists
        self.fieldList = ArrayList()
        self.methodList = ArrayList()
        self.constantPool.clearConstantPool()
        self.constantPool.createPrintLineEntries()
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
        print("Encountered classdeclextends")
        # Clear out global ArrayLists
        self.fieldList = ArrayList()
        self.methodList = ArrayList()
        self.constantPool.clearConstantPool()
        self.constantPool.createPrintLineEntries()
        # Handle class fields
        for x in range(0, node.vl.size()):
            node.vl.elementAt(x).accept(self)
        # Handle class methods
        for x in range(0, node.ml.size()):
            node.ml.elementAt(x).accept(self)
        classIndex = self.constantPool.getClass(node.i.s)
        self.codeGen.addClass(ClassFile(classIndex, 2, self.constantPool.getCPClone(), self.fieldList, self.methodList))
    
    @vis.when(mjc_ClassDeclList)
    def visit(self, node):
        #if node.size() != 0:
        #    addInit()
        for x in range(0, node.size()):
            node.elementAt(x).accept(self)
        self.codeGen.writeFiles()
