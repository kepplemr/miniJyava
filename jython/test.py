'''
Created on Nov 14, 2013

@author: michael
'''
#from CodeGenVisitor import CodeGenVisitor
import sys
from os.path import dirname, realpath, sep, pardir
temp = sep + pardir + sep + pardir + sep + pardir + sep
sys.path.append(dirname(realpath(__file__)) + temp + "classes")
from javacode import *
from javacode.symbol import *
from javacode.syntaxtree import *
#lib_path = os.path.abspath('../../classes')
#sys.path.append(lib_path)

print(sys.path)
print("sdsdddddddddddddddddd")