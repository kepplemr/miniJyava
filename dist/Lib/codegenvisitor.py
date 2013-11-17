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
from javacode import *
from javacode.symbol import *
from javacode.syntaxtree import *
from javacode.classwriter import *
from javacode.classwriter.constantpool import *

class CodeGenVisitor(VisitorAdaptor):
    #ACCESS_PUBLIC = 1
    codeGen = CodeGenerator()
    constantPool = ConstantPoolIndexer()
    fieldList = ArrayList()
    methodList = ArrayList()
    
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
        #nameIndex = self.constantPool.getUtf8(node.t.toString())
        #typeIndex = self.constantPool.getUtf8(node.i.toString())
        #field = FieldInfo(self.ACCESS_PUBLIC, nameIndex, typeIndex)
        #self.fieldList.add(field)
        
    @vis.when(mjc_MethodDeclSimple)
    def visit(self, node):
        print("Encountered MethodDeclSimple")
        
    @vis.when(mjc_MethodDeclStatic)
    def visit(self, node):
        print("Encountered MethodDeclStatic")
          
    @vis.when(mjc_ClassDeclSimple)
    def visit(self,node):
        print("Encountered classdecl")
        # Clear out global ArrayLists
        self.fieldList = ArrayList()
        self.methodList = ArrayList()
        self.constantPool.clearConstantPool()
        self.constantPool.createPrintLineEntries()
        # Handle class fields
        #for x in range(0, node.vl.size()):
        #    node.vl.elementAt(x).accept(self)
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
        #for x in range(0, node.vl.size()):
        #    node.vl.elementAt(x).accept(self)
        classIndex = self.constantPool.getClass(node.i.s)
        self.codeGen.addClass(ClassFile(classIndex, 2, self.constantPool.getCPClone(), self.fieldList, self.methodList))
    
    @vis.when(mjc_ClassDeclList)
    def visit(self, node):
        for x in range(0, node.size()):
            node.elementAt(x).accept(self)
        self.codeGen.writeFiles()
