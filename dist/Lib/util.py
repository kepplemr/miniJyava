'''
Created on Nov 18, 2013

@author: michael
'''
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
    