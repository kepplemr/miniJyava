package syntaxtree;

/* This is a classgen file.  From this file the Classgen framework
   will automatically generate every node in your syntax tree.

   The file format is fairly simple.  There are a few descriptive
   comments in this file to help you, dear reader, understand the
   file.  For a more detailed treatment, please see the classgen
   website: http://classgen.sourceforge.net/docs/lang1.html

*/

/*
  This stanza declares the class mjc_ClassDecl with two subclasses.

  Note "mjc_ClassDecl" is in quotes.  If it were not in quotes,
  Classgen would rename the file to Mjc_ClassDecl to comply with
  Java's naming conventions.
*/

"mjc_ClassDecl" ::= 	{"mjc_ClassDeclExtends"} /* Declaring a subclass */
                                "mjc_Identifier":i  
				    /* Declaring an identifier in the
				     * subclass.  "mjc_Identifier" is
				     * its type, i is its real
				     * variable name */
				"mjc_Identifier":j
				"mjc_VarDeclList":vl
				"mjc_MethodDeclList":ml
			| {"mjc_ClassDeclSimple"} /* Another subclass, notice the |,
						     which separates subclasses */
				"mjc_Identifier":i
				"mjc_VarDeclList":vl
				"mjc_MethodDeclList":ml

"mjc_Exp" ::=		 {"mjc_And"}
				"mjc_Exp":e1
				"mjc_Exp":e2
			|{"mjc_ArrayLength"}
				"mjc_Exp":e
			|{"mjc_ArrayLookup"}
				"mjc_Exp":e1
				"mjc_Exp":e2
			|{"mjc_CallExpression"}
				"mjc_Exp":e
				"mjc_Identifier":i
				"mjc_ExpList":el
			|{"mjc_DoubleEqual"}
				"mjc_Exp":e1
				"mjc_Exp":e2
                        |{"mjc_GTEQ"}
                                "mjc_Exp":e1
                                "mjc_Exp":e2
                        |{"mjc_LTEQ"}
                                "mjc_Exp":e1
                                "mjc_Exp":e2
            |{"mjc_NotEqual"}
                "mjc_Exp":e1
                "mjc_Exp":e2
			|{"mjc_False"}
			|{"mjc_IdentifierExp"}
				string:s
			|{"mjc_IntegerLiteral"}
				"int":i
			|{"mjc_StringLiteral"}
				string:s
			|{"mjc_NewArray"}
				"mjc_Exp":e
			|{"mjc_NewObject"}
				"mjc_Identifier":i
			|{"mjc_Not"}
				"mjc_Exp":e
			|{"mjc_Or"}
				"mjc_Exp":e1
				"mjc_Exp":e2
			|{"mjc_This"}
                "mjc_Identifier":i
			|{"mjc_Null"}			
			|{"mjc_True"}
			|{"mjc_Add"}
				"mjc_Exp":e1
				"mjc_Exp":e2
			|{"mjc_Div"}
				"mjc_Exp":e1
				"mjc_Exp":e2
			|{"mjc_GT"}
				"mjc_Exp":e1
				"mjc_Exp":e2
			|{"mjc_LT"}
				"mjc_Exp":e1
				"mjc_Exp":e2
			|{"mjc_Mult"}
				"mjc_Exp":e1
				"mjc_Exp":e2
			|{"mjc_Sub"}
				"mjc_Exp":e1
				"mjc_Exp":e2

"mjc_Statement" ::=	{"mjc_ArrayAssign"}
				"mjc_Identifier":i
				"mjc_Exp":e1
				"mjc_Exp":e2
			|{"mjc_Assign"}
				"mjc_Identifier":i
				"mjc_Exp":e
			|{"mjc_Block"}
				"mjc_StatementList":sl
			|{"mjc_CallStatement"}
				"mjc_Exp":e
				"mjc_Identifier":i
				"mjc_ExpList":el
			|{"mjc_If"}	
				"mjc_Exp":e
				"mjc_Statement":s1
				"mjc_Statement":s2
			|{"mjc_Print"}
				"mjc_Exp":e
			|{"mjc_While"}	
				"mjc_Exp":e
				"mjc_Statement":s

"mjc_Type" ::= 	{"mjc_BooleanType"}
		|{"mjc_IdentifierType"}
			string:as
		|{"mjc_IntArrayType"}
		|{"mjc_StringArrayType"}
		|{"mjc_IntegerType"}
		|{"mjc_StringType"}

"mjc_MethodType" ::= 	{"mjc_MethodVoidType"}
			| {"mjc_MethodReturnType"}
				"mjc_Type":t
	
"mjc_Formal" ::= 	"mjc_Type":t
			"mjc_Identifier":i

"mjc_Identifier" ::= 	string:s

"mjc_MethodDecl" ::=	{"mjc_MethodDeclSimple"}
				"mjc_MethodType":t
				"mjc_Identifier":i
				"mjc_FormalList":fl
				"mjc_VarDeclList":vl
				"mjc_StatementList":sl
				"mjc_Exp":e
			| {"mjc_MethodDeclStatic"}
				"mjc_MethodType":t
				"mjc_Identifier":i
				"mjc_FormalList":fl
				"mjc_VarDeclList":vl
				"mjc_StatementList":sl
				"mjc_Exp":e
		
"mjc_Program" ::=	"mjc_ClassDeclList":cl

"mjc_VarDecl" ::=	"mjc_Type":t
			"mjc_Identifier":i

"mjc_Operator" ::=      {"mjc_Op_LTEQ"}
               |        {"mjc_Op_GTEQ"}
               |        {"mjc_Op_NEQ"}
               |        {"mjc_Op_EQ"}
               |        {"mjc_Op_LT"}
               |        {"mjc_Op_GT"}
               |        {"mjc_Op_MINUS"}
               |        {"mjc_Op_DIV"}
               |        {"mjc_Op_MUL"}
               |        {"mjc_Op_ADD"}

/*  Below are all lists, notice the * being used like a kleene
    closure */

"mjc_ClassDeclList" ::= "mjc_ClassDecl"*
"mjc_ExpList" ::= "mjc_Exp"*
"mjc_FormalList" ::= "mjc_Formal"*
"mjc_MethodDeclList" ::= "mjc_MethodDecl"*
"mjc_StatementList" ::= "mjc_Statement"*
"mjc_VarDeclList" ::= "mjc_VarDecl"*
