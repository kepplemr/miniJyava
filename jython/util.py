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
EXP_OBJECT = 0
EXP_IMMSTRREF = 1
EXP_INTINDEX = 2
EXP_STRINDEX = 3
EXP_LOCINTIND = 4
EXP_LOCSTRIND = 5
EXP_LOCOBJECT = 6
EXP_IMMINTVAL = 7
EXP_BOOLVAL = 8
EXP_NEWARRAY = 9
EXP_INTARRAY = 10
EXP_STRARRAY = 11
EXP_IDENTIFIER = 12

EXP_FIELD_INT = 13
EXP_FIELD_STRING = 14
EXP_FIELD_OBJECT = 15
EXP_FIELD_BOOL = 18

EXP_IMMBOOL = 16
EXP_LOCBOOL = 17

""" Converts long toString() from ClassGen files to more sensical format """
def typeConvert(mjc_Type):
    mjc_Type = mjc_Type.strip()
    if mjc_Type[:15] == "mjc_StringArray":
        return "[Ljava/lang/String;"
    elif mjc_Type[:10] == "mjc_String":
        return "Ljava/lang/String;"
    elif mjc_Type[:12] == "mjc_IntArray":
        return "[I"
    elif mjc_Type[:11] == "mjc_Integer":
        return "I"
    elif (mjc_Type[:15] == "mjc_BooleanType" or mjc_Type[:8] == "mjc_True" or
          mjc_Type[:9] == "mjc_False"):
        return "Z"
    elif mjc_Type[:18] == "mjc_IdentifierType":
        start = mjc_Type.index('(') + len('(')
        end = mjc_Type.index(')', start)
        return mjc_Type[start:end].strip()
    elif mjc_Type[:14] == "mjc_Identifier":
        start = mjc_Type.index('(') + len('(')
        end = mjc_Type.index(')', start)
        return mjc_Type[start:end].strip()
    elif mjc_Type[:20] == "mjc_MethodReturnType":
        start = mjc_Type.index('(') + len('(')
        end = mjc_Type.index(')', start)+1
        type = mjc_Type[start:end].strip()
        return typeConvert(type)
    else:
        return "V"
    
""" Converts string representation of type to constant value """
def setType(codeGen, typeString):
    # class field
    if typeString[:3] == "<f>":
        type = typeString[3:]
        if type == "I" or type == "[I":
            codeGen.expType = EXP_FIELD_INT
        elif type == "[Ljava/lang/String;" or type == "Ljava/lang/String;":
            codeGen.expType = EXP_FIELD_STRING
        elif type == "Z":
            codeGen.expType = EXP_FIELD_BOOL
        else:
            codeGen.expType = EXP_FIELD_OBJECT
    elif typeString == "I":
        codeGen.expType = EXP_LOCINTIND
    elif typeString == "Ljava/lang/String;":
        codeGen.expType = EXP_LOCSTRIND
    elif typeString == "[I":
        codeGen.expType = EXP_INTARRAY
    elif typeString == "[Ljava/lang/String;":
        codeGen.expType = EXP_STRARRAY
    elif typeString == "Z":
        codeGen.expType = EXP_LOCBOOL
    # Object reference
    else:
        codeGen.expType = EXP_LOCOBJECT

    
""" Functions for finding identifiers in the symbol table with precedence 
    fields -> method parameters -> method locals and accessing their info. """
def getVariable(codeGen, classSym, methodSym, variable):
    currSym = Symbol.symbol(mjc_Identifier(variable).toString())
    if typeConvert(currSym.toString()) == "void":
        return FieldEntry("void", mjc_IdentifierType("void"))
    fieldEntry = None
    fieldEntry = codeGen.symTab.getField(classSym, currSym)
    if fieldEntry is not None:
        return fieldEntry
    fieldEntry = codeGen.symTab.getMethodParam(classSym, methodSym, currSym)
    if fieldEntry is not None:
        return fieldEntry
    fieldEntry = codeGen.symTab.getMethodLocal(classSym, methodSym, currSym)
    return fieldEntry
def getType(codeGen, classSym, methodSym, variable):
    fieldEntry = getVariable(codeGen, classSym, methodSym, variable)
    if isField(fieldEntry):
        return ("<f>" + typeConvert(fieldEntry.getType().toString()))
    return typeConvert(fieldEntry.getType().toString())
def getObjType(codeGen, classSym, methodSym, variable):
    fieldEntry = getVariable(codeGen, classSym, methodSym, variable)
    return ("L" + typeConvert(fieldEntry.getType().toString()) + ";")
def getLocation(codeGen, classSym, methodSym, variable):
    fieldEntry = getVariable(codeGen, classSym, methodSym, variable)
    if fieldEntry is None:
        return 0
    if isField(fieldEntry):
        type = typeConvert(fieldEntry.getType().toString())
        cpIndex = codeGen.constantPool.getFieldInfo(classSym.toString(), variable, type)
        return cpIndex
    return fieldEntry.getLocation()

def isObject(arg):
    if arg[:18] == "mjc_IdentifierType" or arg[:14] == "mjc_Identifier":
        return True
    else:
        return False
def isField(arg):
    isField = True if arg.getLocation() == -1 else False
    return isField
    
    
""" Handles putting stuff on stack according to type """
def pushToStack(codeGen, type, value, arrayType):
    if (type == EXP_FIELD_INT or type == EXP_FIELD_STRING or 
        type == EXP_FIELD_OBJECT or type == EXP_FIELD_BOOL):
        loadInstance(codeGen)
        # getfield <cpIndexToFieldRef>
        codeGen.code.add(0xb4)
        codeGen.code.add(0x00)
        codeGen.code.add(value)
    elif type == EXP_LOCBOOL:
        # iload <local bool>
        codeGen.code.add(0x15)
        codeGen.code.add(value)
    elif type == EXP_INTINDEX or type == EXP_STRINDEX:
        # ldc <cpIntIndex>
        codeGen.code.add(0x12)
        codeGen.code.add(value)
    elif type == EXP_LOCINTIND:
        # iload <local>
        codeGen.code.add(0x15)
        codeGen.code.add(value)
    elif type == EXP_LOCSTRIND or type == EXP_LOCOBJECT:
        # aload <local>
        codeGen.code.add(0x19)
        codeGen.code.add(value)
    elif type == EXP_INTARRAY:
        # iaload
        codeGen.code.add(0x2e)
        codeGen.expType = EXP_IMMINTVAL
    elif type == EXP_STRARRAY:
        # aaload
        codeGen.code.add(0x32)
        codeGen.expType = EXP_IMMSTRREF
    elif type == EXP_IMMINTVAL or type == EXP_IMMSTRREF or type == EXP_IMMBOOL:
        # already on stack, no need to push anything
        pass
    elif type == EXP_NEWARRAY:
        if arrayType == "[I":
            # ldc <size>
            codeGen.code.add(0x12)
            codeGen.code.add(value)
            # newarray(int)
            codeGen.code.add(0xbc)
            codeGen.code.add(0x0a)
        else:
            # push size of array to stack
            codeGen.code.add(0x12)
            codeGen.code.add(value)
            # anewarray (String class)
            codeGen.code.add(0xbd)
            strInd = codeGen.constantPool.getClass("java/lang/String")
            codeGen.code.add(0x00)
            codeGen.code.add(strInd)
    elif type == EXP_OBJECT:
        pass
    else:
        print("Unexpected push index -> " + repr(type))
        

""" Handles storing stuff to locals according to type """
# BOOLVAL & IDENTIFIER & IMMBOOL
def popToLocal(codeGen, type, location):
    if (type == EXP_FIELD_INT or type == EXP_FIELD_STRING or 
        type == EXP_FIELD_OBJECT  or type == EXP_FIELD_BOOL):        
        # putfield <cpIndexToFieldRef>
        codeGen.code.add(0xb5)
        codeGen.code.add(0x00)
        codeGen.code.add(location)
    elif (type == EXP_INTINDEX or type == EXP_LOCINTIND or type == EXP_IMMINTVAL or
          type == EXP_LOCBOOL):
        # istore <location>
        codeGen.code.add(0x36)
        codeGen.code.add(location)
    elif (type == EXP_OBJECT or type == EXP_STRINDEX or type == EXP_IMMSTRREF or 
          type == EXP_NEWARRAY or type == EXP_LOCOBJECT or type == EXP_LOCSTRIND):
        # astore <location>
        codeGen.code.add(0x3a)
        codeGen.code.add(location)
    elif type == EXP_INTARRAY:
        # iastore
        codeGen.code.add(0x4f)
    elif type == EXP_STRARRAY:
        # aastore
        codeGen.code.add(0x53)
    else:
        print("Unexpected pop index -> " + repr(type))

""" Invokes virtual function in code """
def invokeVirtual(codeGen, methRef):
    # invokevirtual <method>
    codeGen.code.add(0xb6)
    codeGen.code.add(0x00)
    codeGen.code.add(methRef)

""" Print functions """
def printPush(codeGen, virtual):
    pushToStack(codeGen, codeGen.expType, codeGen.expIndex, None)
    invokeVirtual(codeGen, virtual)
def printImm(codeGen, virtual):
    invokeVirtual(codeGen, virtual)

""" Expression evaluation functions """
def arithmeticExpression(codeGen, mjc_Exp, mjc_OpType):
    codeGen.expIndex = 0
    # push both EXP's to stack
    mjc_Exp.e1.accept(codeGen)
    pushToStack(codeGen, codeGen.expType, codeGen.expIndex, None)
    mjc_Exp.e2.accept(codeGen)
    pushToStack(codeGen, codeGen.expType, codeGen.expIndex, None)
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
    pushToStack(codeGen, codeGen.expType, codeGen.expIndex, None)    
    mjc_Exp.e2.accept(codeGen)
    pushToStack(codeGen, codeGen.expType, codeGen.expIndex, None)
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
    codeGen.expType = EXP_IMMBOOL
        
""" Adds default <init> constructor """
def addInit(codeGen):
    codeGen.code = ArrayList()
    loadInstance(codeGen)
    # invokespecial #1
    codeGen.code.add(0xb7)
    codeGen.code.add(0x00)
    codeGen.code.add(0x06)
    # Print message to indicate constructor was called.
    codeGen.code.add(0xb2)
    codeGen.code.add(0x00)
    codeGen.code.add(0x0d)
    codeGen.code.add(0x12)
    codeGen.code.add(0x1c)
    codeGen.code.add(0xb6)
    codeGen.code.add(0x00)
    codeGen.code.add(0x19)
    # return
    codeGen.code.add(0xb1)
    init = MethodInfo(0, 3, 4, 7, codeGen.code.size() + 12, 512, 512, codeGen.code)
    codeGen.methodList.add(init)
    
""" Puts current object reference on stack """
def loadInstance(codeGen):
    codeGen.code.add(0x2a)
    
""" Handle the calculation/encoding of method return value in called method """
def handleReturn(codeGen, mjc_Method):
    mjc_Method.e.accept(codeGen)
    ret = typeConvert(mjc_Method.t.toString())
    if ret == "V":
        # empty return opcode
        codeGen.code.add(0xb1)
    elif ret == "I" or ret == "Z":
        pushToStack(codeGen, codeGen.expType, codeGen.expIndex, None)
        # ireturn
        codeGen.code.add(0xac)
    elif ret == "[Ljava/lang/String;" or ret == "[I":
        pushToStack(codeGen, EXP_LOCOBJECT, codeGen.expIndex, None)
        # areturn
        codeGen.code.add(0xb0)
    elif ret == "Ljava/lang/String;":
        pushToStack(codeGen, codeGen.expType, codeGen.expIndex, None)
        # areturn
        codeGen.code.add(0xb0)
    # Object
    else:
        pushToStack(codeGen, EXP_LOCOBJECT, codeGen.expIndex, None)
        # areturn
        codeGen.code.add(0xb0)
               

""" Create/return CP reference to methodRef entry """    
def getMethodReference(codeGen, invokedObj): 
    if isinstance(invokedObj.e, mjc_IdentifierExp):
        variable = getVariable(codeGen, codeGen.classSym, codeGen.methodSym, invokedObj.e.s)
        className = typeConvert(variable.toString())       
    else:
        className = codeGen.classSym.toString()
    methodName = invokedObj.i.toString()
    method = codeGen.symTab.getMethod(Symbol.symbol(className), Symbol.symbol(methodName))
    retType = typeConvert(method.getResult())
    if retType == "I":
        codeGen.expType = EXP_IMMINTVAL
        codeGen.expList += typeConvert(method.getResult())
    elif retType == "[I":
        codeGen.expType = EXP_OBJECT
        codeGen.expList += typeConvert(method.getResult())
    elif retType == "Ljava/lang/String;":
        codeGen.expType = EXP_IMMSTRREF
        codeGen.expList += typeConvert(method.getResult())
    elif retType == "[Ljava/lang/String;":
        codeGen.expType = EXP_OBJECT
        codeGen.expList += typeConvert(method.getResult())
    elif retType == "Z":
        codeGen.expType = EXP_IMMBOOL
        codeGen.expList += typeConvert(method.getResult())
    elif retType == "V":
        codeGen.expType = EXP_IMMINTVAL
        codeGen.expList += "V"
    # Object return
    else:
        codeGen.expType = EXP_OBJECT
        codeGen.expList += ("L" + typeConvert(method.getResult()) + ";")
    if isinstance(invokedObj, mjc_CallStatement) and retType != "V":
        # pop return, no one cares
        self.code.add(0x57)
    return codeGen.constantPool.getMethodInfo(className, typeConvert(methodName), codeGen.expList)
        
""" Macro class/method/call level functions """ 
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
    mjc_Method.fl.accept(codeGen)
    mjc_Method.t.accept(codeGen)
    nameIndex = codeGen.constantPool.getUtf8(typeConvert(mjc_Method.i.toString()))
    typeIndex = codeGen.constantPool.getUtf8(codeGen.formalList)
    # locals = params + locals + possible return value
    maxLocals = mjc_Method.fl.size() + mjc_Method.vl.size() + 1
    # Handle method statements
    for x in range(0, mjc_Method.sl.size()):
        mjc_Method.sl.elementAt(x).accept(codeGen)
    handleReturn(codeGen, mjc_Method)
    if mjc_MethType == "static":
        method = MethodInfo(codeGen.ACCESS_PUBLICSTATIC, nameIndex, typeIndex, codeGen.CODE_INDEX, codeGen.code.size()+12, codeGen.MAX_STACK, maxLocals, codeGen.code)
    else:
        method = MethodInfo(codeGen.ACCESS_PUBLIC, nameIndex, typeIndex, codeGen.CODE_INDEX, codeGen.code.size()+12, codeGen.MAX_STACK, maxLocals, codeGen.code)
    codeGen.methodList.add(method)
def getCall(codeGen, call, location):
    pushToStack(codeGen, EXP_LOCOBJECT, location, None)
    # Create method type based off ExpList arguments and push them on stack
    call.el.accept(codeGen);
    methRef = getMethodReference(codeGen, call) 
    invokeVirtual(codeGen, methRef)