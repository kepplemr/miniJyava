'''
Created on Nov 18, 2013

@author: michael
'''
import struct
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

# Constants
EXP_IMMSTRREF = 1
EXP_INTINDEX = 2
EXP_STRINDEX = 3
EXP_LOCINTIND = 4
EXP_LOCSTRIND = 5
EXP_IMMINTVAL = 6
EXP_BOOLVAL = 7
EXP_ARRAY = 8
EXP_INTARRAY = 9
EXP_STRARRAY = 10

""" Converts long toString() from ClassGen files to more sensical format """
def typeConvert(mjc_Type):
    if mjc_Type[:19] == "mjc_StringArrayType":
        return "[Ljava/lang/String;"
    elif mjc_Type[:14] == "mjc_StringType":
        return "Ljava/lang/String;"
    elif mjc_Type[:16] == "mjc_IntArrayType":
        return "[I"
    elif mjc_Type[:15] == "mjc_IntegerType":
        return "I"
    elif mjc_Type[:15] == "mjc_BooleanType":
        return "Z"
    elif mjc_Type[:18] == "mjc_IdentifierType":
        start = mjc_Type.index('(') + len('(')
        end = mjc_Type.index(')', start)
        id = mjc_Type[start:end].strip()
        return "L" + id + ";"
    elif mjc_Type[:14] == ("mjc_Identifier"):
        start = mjc_Type.index('(') + len('(')
        end = mjc_Type.index(')', start)
        return mjc_Type[start:end].strip()
    else:
        return "V"
    
""" Print functions for various types """
def printCpIntIndex(codeGen):
    # ldc & index
    codeGen.code.add(0x12)
    codeGen.code.add(codeGen.expIndex)
    # invokevirtual 'println(CP_IntIndex)'
    codeGen.code.add(0xb6)
    codeGen.code.add(0x00)
    codeGen.code.add(0x13)
def printCpStrIndex(codeGen):
    # ldc & index
    codeGen.code.add(0x12)
    codeGen.code.add(codeGen.expIndex)
    # invokevirtual 'println(CP_StrIndex)'
    codeGen.code.add(0xb6)
    codeGen.code.add(0x00)
    codeGen.code.add(0x19)
def printLocInt(codeGen):
    # iload <local>
    codeGen.code.add(0x15)
    codeGen.code.add(codeGen.expIndex)
    # invokevirtual 'println(int i)
    codeGen.code.add(0xb6)
    codeGen.code.add(0x00)
    codeGen.code.add(0x13)
def printLocString(codeGen):
    # aload <local>
    codeGen.code.add(0x19)
    codeGen.code.add(codeGen.expIndex)
    # invokevirtual 'println(String str)'
    codeGen.code.add(0xb6)
    codeGen.code.add(0x00)
    codeGen.code.add(0x19)
def printImmIntVal(codeGen):
    # invokevirtual 'println(42)'
    codeGen.code.add(0xb6)
    codeGen.code.add(0x00)
    codeGen.code.add(0x13)
def printImmBoolVal(codeGen):
    # invokevirtual 'println(boolean)'
    codeGen.code.add(0xb6)
    codeGen.code.add(0x00)
    codeGen.code.add(0x16)

""" Expression evaluation functions """
def arithmeticExpression(codeGen, mjc_Exp, mjc_OpType):
    codeGen.expIndex = 0
    # push both EXP's to stack
    mjc_Exp.e1.accept(codeGen)
    codeGen.code.add(0x12)
    codeGen.code.add(codeGen.expIndex)
    mjc_Exp.e2.accept(codeGen)
    codeGen.code.add(0x12)
    codeGen.code.add(codeGen.expIndex)
    # iadd 
    if mjc_OpType == "Add":
        codeGen.code.add(0x60)
    elif mjc_OpType == "Sub":
        codeGen.code.add(0x64)
    elif mjc_OpType == "Mul":
        codeGen.code.add(0x68)
    elif mjc_OpType == "Div":
        codeGen.code.add(0x6c)  
    codeGen.expType = EXP_IMMINTVAL
def comparisonExpression(codeGen, mjc_Exp, mjc_OpType):
    codeGen.expIndex = 0
    # push both EXP's to stack
    mjc_Exp.e1.accept(codeGen)
    codeGen.code.add(0x12)
    codeGen.code.add(codeGen.expIndex)
    mjc_Exp.e2.accept(codeGen)
    codeGen.code.add(0x12)
    codeGen.code.add(codeGen.expIndex)
    # if_icmp<Op> -> (branch + 8)
    if mjc_OpType == "GT":
        codeGen.code.add(0xa3)
    elif mjc_OpType == "LT":
        codeGen.code.add(0xa1)
    elif mjc_OpType == "GTE":
        codeGen.code.add(0xa2)
    elif mjc_OpType == "LTE":
        codeGen.code.add(0xa4)
    elif mjc_OpType == "EQ":
        codeGen.code.add(0xa5)
    elif mjc_OpType == "NE":
        codeGen.code.add(0xa6)
    codeGen.code.add(0x00)
    codeGen.code.add(0x08)
    # bipush 0
    codeGen.code.add(0x10)
    codeGen.code.add(0x00)
    # goto -> (branch + 5)
    codeGen.code.add(0xa7)
    codeGen.code.add(0x00)
    codeGen.code.add(0x05)
    # bipush 1
    codeGen.code.add(0x10)
    codeGen.code.add(0x01)
    codeGen.expType = EXP_BOOLVAL
        
""" Adds default <init> constructor """
def addInit(codeGen):
    codeGen.code = ArrayList()
    # aload_0
    codeGen.code.add(0x2a)
    # invokespecial #1
    codeGen.code.add(0xb7)
    codeGen.code.add(0x00)
    codeGen.code.add(0x06)
    # return
    codeGen.code.add(0xb1)
    init = MethodInfo(0, 3, 4, 7, codeGen.code.size() + 12, 512, 512, codeGen.code)
    codeGen.methodList.add(init)
   
""" Macro class/method level functions """ 
def getClass(codeGen, mjc_Class, mjc_ClassType):
    # Set class symbol marker
    codeGen.classSym = Symbol.symbol(typeConvert(mjc_Class.i.toString()))
    # Clear out global ArrayLists
    codeGen.fieldList = ArrayList()
    codeGen.methodList = ArrayList()            
    # Get parent class's fields and methods if we're extending something
    if mjc_ClassType == "extends":
        for x in range(0, mjc_Class.j.vl.size()):
            mjc_Class.j.vl.elementAt(x).accept(codeGen)
        for x in range(0, mjc_Class.j.ml.size()):
            mjc_Class.j.ml.elementAt(x).accept(codeGen)
    addInit(codeGen)
    # Handle class fields
    for x in range(0, mjc_Class.vl.size()):
        mjc_Class.vl.elementAt(x).accept(codeGen)
    # Handle class methods
    for x in range(0, mjc_Class.ml.size()):
        mjc_Class.ml.elementAt(x).accept(codeGen)
    classIndex = codeGen.constantPool.getClass(mjc_Class.i.s)
    codeGen.codeGener.addClass(ClassFile(classIndex, 2, codeGen.constantPool.getCPClone(), codeGen.fieldList, codeGen.methodList))
def getMethod(codeGen, mjc_Method, mjc_MethType):
    # Set method symbol marker
    codeGen.methodSym = Symbol.symbol(mjc_Method.i.toString())
    codeGen.code = ArrayList()
    type = "("
    for x in range (0, mjc_Method.fl.size()):
        type += typeConvert(mjc_Method.fl.elementAt(x).t.toString())
    type += ")"
    type += typeConvert(mjc_Method.t.toString())
    nameIndex = codeGen.constantPool.getUtf8(typeConvert(mjc_Method.i.toString()))
    typeIndex = codeGen.constantPool.getUtf8(type)
    maxLocals = mjc_Method.fl.size() + mjc_Method.vl.size()
    # Handle method statements
    for x in range(0, mjc_Method.sl.size()):
        mjc_Method.sl.elementAt(x).accept(codeGen)
    # empty return opcode
    codeGen.code.add(0xb1)
    if mjc_MethType == "static":
        method = MethodInfo(codeGen.ACCESS_PUBLICSTATIC, nameIndex, typeIndex, codeGen.CODE_INDEX, codeGen.code.size()+12, codeGen.MAX_STACK, maxLocals, codeGen.code)
    else:
        method = MethodInfo(codeGen.ACCESS_PUBLIC, nameIndex, typeIndex, codeGen.CODE_INDEX, codeGen.code.size()+12, codeGen.MAX_STACK, maxLocals, codeGen.code)
    codeGen.methodList.add(method)
    
""" Array Creation Functions """
def newStringArray(codeGen, size, location):
    # push size of array to stack
    codeGen.code.add(0x12)
    codeGen.code.add(size)
    # anewarray (String class)
    codeGen.code.add(0xbd)
    strInd = codeGen.constantPool.getClass("java/lang/String")
    codeGen.code.add(0x00)
    codeGen.code.add(strInd)
    # astore <location>
    codeGen.code.add(0x3a)
    codeGen.code.add(location)
def newIntArray(codeGen, size, location):
    codeGen.code.add(0x12)
    codeGen.code.add(size)
    # newarray(int)
    codeGen.code.add(0xbc)
    codeGen.code.add(0x0a)
    # astore <location>
    codeGen.code.add(0x3a)
    codeGen.code.add(location)