'''
Created on Nov 18, 2013

@author: michael
'''
def typeConvert(mjc_Type):
    if mjc_Type[:19] == ("mjc_StringArrayType"):
        return "[Ljava/lang/String;"
    elif mjc_Type == ("mjc_StringType(\n" + ") [mjc_StringType]"):
        return "Ljava/lang/String;"
    elif mjc_Type == ("mjc_IntArrayType(\n" + ") [mjc_IntArrayType]"):
        return "[I"
    elif mjc_Type == ("mjc_IntegerType(\n" + ") [mjc_IntegerType]"):
        return "I"
    elif mjc_Type == ("mjc_BooleanType(\n" + ") [mjc_BooleanType]"):
        return "Z"
    elif mjc_Type[:19] == ("mjc_IndentifierType"):
        return "object"

    