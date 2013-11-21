'''
Created on Nov 18, 2013

@author: michael
'''
EXP_ADD = 0
EXP_SUB = 1
EXP_MUL = 2
EXP_DIV = 3
EXP_GT = 4
EXP_LT = 5
EXP_GTE = 6
EXP_LTE = 7
EXP_EQ = 8
EXP_NE = 9

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
        codeGen.expType = codeGen.EXP_IMMINTVAL
        
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
        codeGen.expType = codeGen.EXP_BOOLVAL