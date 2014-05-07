#!/usr/bin/python
# classReader.py
#
# Author: Michael Kepple
# Note: must be run with python3.3 
import sys
import platform
import struct

codeLocInPool = 0
pad = "    "

""" Processes constant pool entries of various types. Returns number of items
filed on the iteration (long, double will fill two). """
def constPoolEntry(number, myFile):
    print(pad + "Constant pool entry " + repr(number), end=" -> ")
    byteValue = int.from_bytes(myFile.read(1), byteorder='big')
    lpad = pad + pad
    if byteValue == 7:
        print("Class_Info (7)")
        print(lpad + "Name index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    elif byteValue == 9:
        print("Field_Ref (9)")
        print(lpad + "Class index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
        print(lpad + "Name/type index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    elif byteValue == 10:
        print("Method_Ref (10)")
        print(lpad + "Class -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
        print(lpad + "Name/type -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    elif byteValue == 11:
        print("InterfaceMethod_Ref (11)")
        print(lpad + "Class index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
        print(lpad + "Name/type -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    elif byteValue == 8:
        print("String (8)")
        print(lpad + "String index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    elif byteValue == 3:
        print("Integer (3)")
        print(lpad + "Integer value -> " + repr(int.from_bytes(myFile.read(4), byteorder='big')))
    elif byteValue == 4:
        print("Float (4)")
        print(lpad + "Float value -> " + repr(struct.unpack('>f', myFile.read(4))))
    elif byteValue == 5:
        print("Long (5)")
        print(lpad + "Long value -> " + repr(struct.unpack('>q', myFile.read(8))))
        return 2
    elif byteValue == 6:
        print("Double (6)")
        print(lpad + "Double value -> " + repr(struct.unpack('>d', myFile.read(8))))
        return 2
    elif byteValue == 12:
        print("Name/type (12)")
        print(lpad + "Name -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
        print(lpad + "Type -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    elif byteValue == 1:
        print("Utf-8 (1)")
        length = int.from_bytes(myFile.read(2), byteorder='big')
        print(lpad + "Length -> " + repr(length))
        string = myFile.read(length).decode("utf-8")
        if string == "Code":
            global codeLocInPool
            codeLocInPool = number
    return 1
        
def codeEntry(length, myFile):
    lpad = pad + pad + pad + pad
    print(lpad + "*Code Attribute*")
    print(lpad + "Max Stack -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    print(lpad + "Max Locals -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    codeLength = int.from_bytes(myFile.read(4), byteorder='big')
    print(lpad + "Code length -> " + repr(codeLength))
    print(lpad + "Code -> " + hex(int.from_bytes(myFile.read(codeLength), byteorder='big')))
    exceptionCount = int.from_bytes(myFile.read(2), byteorder='big')
    print(lpad + "Exception count -> " + repr(exceptionCount))
    for _ in range(0, exceptionCount):
        print(lpad + pad + "Skipping exception (8 bytes)")
        myFile.read(8)
    codeAttrCount = int.from_bytes(myFile.read(2), byteorder='big')
    print(lpad + "Attributes count -> " + repr(codeAttrCount))
    for x in range(0, codeAttrCount):
        attributeEntry(x, myFile, 5)
    
def attributeEntry(number, myFile, tabs):
    lpad = ""
    for _ in range(0, tabs):
        lpad += pad
    print(lpad + "Attribute " + repr(number))
    attrName = int.from_bytes(myFile.read(2), byteorder='big')
    attrLength = int.from_bytes(myFile.read(4), byteorder='big')
    print(lpad + pad + "Name index -> " + repr(attrName))
    print(lpad + pad + "Attribute length -> " + repr(attrLength))
    if attrName == codeLocInPool:
        codeEntry(attrLength, myFile)
    else:
        print(lpad + pad + "Skipping attribute bytes -> " + repr(attrLength))
        myFile.read(attrLength)
       
def methodEntry(number, myFile):
    lpad = pad + pad
    print(pad + "Method " + repr(number))
    print(lpad + "Access flags -> " + hex(int.from_bytes(myFile.read(2), byteorder='big')))
    print(lpad + "Name index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    print(lpad + "Type index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    methAttrCount = int.from_bytes(myFile.read(2), byteorder='big')
    print(lpad + "Attributes count -> " + repr(methAttrCount))
    for x in range(0, methAttrCount):
        attributeEntry(x, myFile, 3)
           
def fieldEntry(number, myFile):
    lpad = pad + pad
    print(pad + "Field entry " + repr(number))
    print(lpad + "Access flags -> " + hex(int.from_bytes(myFile.read(2), byteorder='big')))
    print(lpad + "Name index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    print(lpad + "Type index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
    attributesCount = int.from_bytes(myFile.read(2), byteorder='big')
    print(lpad + "Attributes count -> " + repr(attributesCount))
    for x in range(0, attributesCount):
        attributeEntry(x, myFile, 2)

def main():  
    print("Python version -> " + sys.version)
    print("Platform -> " + str(platform.python_implementation()))
    print("Examining file -> " + sys.argv[1]);
    with open(sys.argv[1], "rb") as myFile:
        print("Magic Number -> " + hex(int.from_bytes(myFile.read(4), byteorder='big')))
        print("Minor Number -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
        print("Major Number -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
        consPoolCount = int.from_bytes(myFile.read(2), byteorder='big')
        print("Number of items in constant pool -> " + repr(consPoolCount))
        x = 1
        while x < consPoolCount:
            x += constPoolEntry(x, myFile)
        print("Code location in pool -> " + repr(codeLocInPool))
        print("Access flags -> " + hex(int.from_bytes(myFile.read(2), byteorder='big')))
        print("Class index -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
        print("Super class -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
        interfaceCount = int.from_bytes(myFile.read(2), byteorder='big')
        print("Interface count -> " + repr(interfaceCount))
        for x in range(1, interfaceCount):
            print(pad + "Interface -> " + repr(int.from_bytes(myFile.read(2), byteorder='big')))
        fieldsCount = int.from_bytes(myFile.read(2), byteorder='big')
        print("Fields count -> " + repr(fieldsCount))
        for x in range(0, fieldsCount):
            fieldEntry(x, myFile)
        methodsCount = int.from_bytes(myFile.read(2), byteorder='big')
        print("Method count -> " + repr(methodsCount))
        for x in range(0, methodsCount):
            methodEntry(x, myFile)
        classAttrCount = int.from_bytes(myFile.read(2), byteorder='big')
        print("Class attributes -> " + repr(classAttrCount))
        for x in range(0, classAttrCount):
            attributeEntry(x, myFile, 1)
            
if __name__ == "__main__":
    main()