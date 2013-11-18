'''
Created on Nov 18, 2013

@author: michael
'''
def typeConvert(mjc_Type):
    if mjc_Type[:19] == ("mjc_StringArrayType"):
        return "[Ljava/lang/String;"
    elif mjc_Type[:14] == ("mjc_StringType"):
        return "Ljava/lang/String;"
    elif mjc_Type[:16] == ("mjc_IntArrayType"):
        return "[I"
    elif mjc_Type[:15] == ("mjc_IntegerType"):
        return "I"
    elif mjc_Type[:15] == ("mjc_BooleanType"):
        return "Z"
    elif mjc_Type[:19] == ("mjc_IndentifierType"):
        start = s.index('(') + len('(')
        end = s.index(')', start)
        return "L" + mjc_Type[start:end] + ";"

    