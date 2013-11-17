'''
Created on Nov 14, 2013

@author:      michael
@description: Visitor class used to generate MiniJava bytecode
'''
import sys
import dispatch as vis
from os.path import dirname, realpath, sep, pardir
temp = sep + pardir + sep + pardir + sep + pardir + sep
sys.path.append(dirname(realpath(__file__)) + temp + "classes")
import java.util.ArrayList as ArrayList
from javacode import *
from javacode.symbol import *
from javacode.syntaxtree import *
from javacode.classwriter import *
from javacode.classwriter.constantpool import *

class CodeGenVisitor(VisitorAdaptor):
    codeGen = CodeGenerator()
    constantPool = ConstantPoolIndexer()
    
    # Constructor
    def __init__(self):
        print("Created, yo")  
        
    @vis.on('node')
    def visit(self, node):
        """
        This is the generic method that initializes the
        dynamic dispatcher.
        """
        
    @vis.when(mjc_ClassDeclSimple)
    def visit(self,node):
        print("Encountered classdecl")
        self.constantPool.clearConstantPool()
        self.constantPool.createPrintLineEntries()
        classIndex = self.constantPool.getClass(node.i.s)
        fieldList = ArrayList()
        methodList = ArrayList()
        self.codeGen.addClass(ClassFile(classIndex, 2, self.constantPool.getCPClone(), fieldList, methodList))
        
    @vis.when(mjc_ClassDeclExtends)
    def visit(self, node):
        print("Encountered classdeclextends")
        self.constantPool.clearConstantPool()
        self.constantPool.createPrintLineEntries()
        classIndex = self.constantPool.getClass(node.i.s)
        fieldList = ArrayList()
        methodList = ArrayList()
        self.codeGen.addClass(ClassFile(classIndex, 2, self.constantPool.getCPClone(), fieldList, methodList))
    
    @vis.when(mjc_ClassDeclList)
    def visit(self, node):
        for x in range(0, node.size()):
            node.elementAt(x).accept(self)
        self.codeGen.writeFiles()
