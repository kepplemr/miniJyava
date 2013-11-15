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
from javacode import *
from javacode.symbol import *
from javacode.syntaxtree import *

class CodeGenVisitor(VisitorAdaptor):
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
    
    @vis.when(mjc_ClassDeclList)
    def visit(self, node):
        print("asa")
