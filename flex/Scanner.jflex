package javacode;
import java_cup.runtime.*;

%%

%class Lexer
%cup
%implements sym
%line
%column

%{
    private static int num_nested_comments = 0;
    private Symbol symbol(int sym) 
    {
        return new Symbol(sym, yyline+1, yycolumn+1);
    }
 
    private Symbol symbol(int sym, Object val) 
    {
        return new Symbol(sym, yyline+1, yycolumn+1, val);
    }
 
    private void error(String message) 
    {
        System.out.println("Error at line "+(yyline+1)+", column "+(yycolumn+1)+" : "+message);
    }
%}

LineTerminator  = \r|\n|\r\n
WhiteSpace      = {LineTerminator} | [ \t\f]
Integer         = [0-9]+
String          = \".*\"
ID              = [:jletter:][:jletterdigit:]*
Comment  = "/*" [^*] ~"*/" | "//" .* {LineTerminator}

%%
<YYINITIAL> {
    "beginvars"             {return symbol(BEGINVARS_TOK); }
    "boolean"               {return symbol(BOOLTYPE_TOK); }
    "class"                 {return symbol(CLASS_TOK); }
    "else"                  {return symbol(ELSE_TOK); }
    "endvars"               {return symbol(ENDVARS_TOK); }
    "extends"               {return symbol(EXTENDS_TOK); }
    "false"                 {return symbol(FALSE_TOK); }
    "if"                    {return symbol(IF_TOK); }
    "int"                   {return symbol(INTTYPE_TOK); }
    "length"                {return symbol(LENGTH_TOK); }
    "new"                   {return symbol(NEW_TOK); }
    "null"                  {return symbol(NULL_TOK); }
    "public"                {return symbol(PUBLIC_TOK); }
    "return"                {return symbol(RETURN_TOK); }
    "static"                {return symbol(STATIC_TOK); }
    "String"                {return symbol(STRING_TOK); }
    "System.out.println"    {return symbol(PRINT_TOK); }
    "this"                  {return symbol(THIS_TOK); }
    "true"                  {return symbol(TRUE_TOK); }
    "void"                  {return symbol(VOID_TOK); }
    "while"                 {return symbol(WHILE_TOK); }
    "("                     {return symbol(LPAREN_TOK); }
    ")"                     {return symbol(RPAREN_TOK); }
    "{"                     {return symbol(LBRACE_TOK); }
    "}"                     {return symbol(RBRACE_TOK); }
    "["                     {return symbol(LBRACKET_TOK); }
    "]"                     {return symbol(RBRACKET_TOK); }
    ";"                     {return symbol(SEMICOLON_TOK); }
    ","                     {return symbol(COMMA_TOK); }
    "!"                     {return symbol(BANG_TOK); }
    "+"                     {return symbol(PLUS_TOK); }
    "-"                     {return symbol(MINUS_TOK); }
    "*"                     {return symbol(MUL_TOK); }
    "/"                     {return symbol(DIV_TOK); }
    ">"                     {return symbol(GT_TOK); }
    "<"                     {return symbol(LT_TOK); }
    "."                     {return symbol(DOT_TOK); }
    "="                     {return symbol(ASSIGN_TOK); }
    "&&"                    {return symbol(AND_TOK); }
    "=="                    {return symbol(EQ_TOK); }
    "!="                    {return symbol(NEQ_TOK); }
    ">="                    {return symbol(GTEQ_TOK); }
    "<="                    {return symbol(LTEQ_TOK); }
    {ID}                    {return symbol(ID_TOK, yytext()); }
    {Integer}               {return symbol(INTCONST_TOK, new Integer(yytext())); }
    {String}                {return symbol(STRCONST_TOK, yytext()); }
    {WhiteSpace}+           { }
    {Comment}               { }
}

