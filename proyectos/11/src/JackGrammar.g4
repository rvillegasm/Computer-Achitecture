/** 
    File containing the grammar for the Jack Programming language.
    It is designed to be used with antlr4 in order to generate a parser and a lexer for said language.
 */
grammar JackGrammar;

/**
    Parser rules
 */

// program structure
classNT : 'class' classNameNT '{' classVarDecNT* subroutineDecNT* '}' ;

classVarDecNT : ('static'|'field') typeNT varNameNT (',' varNameNT)* ';' ;

typeNT : 'int'|'char'|'boolean'|classNameNT ;

subroutineDecNT : ('constructor'|'function'|'method') ('void'|typeNT) subroutineNameNT '(' parameterListNT ')' subroutineBodyNT ;

parameterListNT : ((typeNT varNameNT) (',' typeNT varNameNT)*)? ;

subroutineBodyNT : '{' varDecNT* statementsNT '}' ;

varDecNT : 'var' typeNT varNameNT (',' varNameNT)* ';' ;

classNameNT : IDENTIFIER ;

subroutineNameNT : IDENTIFIER ;

varNameNT : IDENTIFIER ;

// statements
statementsNT : statementNT* ;

statementNT : letStatementNT
            | ifStatementNT
            | whileStatementNT
            | doStatementNT
            | returnStatementNT 
            ;

letStatementNT : 'let' varNameNT ('[' expressionNT ']' )? '=' expressionNT ';' ;

ifStatementNT : 'if' '(' expressionNT ')' '{' statementsNT '}' ('else' '{' statementsNT '}')? ;

whileStatementNT : 'while' '(' expressionNT ')' '{' statementsNT '}' ;

doStatementNT : 'do' subroutineCallNT ';' ;

returnStatementNT : 'return' expressionNT? ';' ;

// expressions
expressionNT : termNT (opNT termNT)* ;

termNT : INTEGERCONSTANT 
       | STRINGCONSTANT 
       | keywordConstantNT 
       | varNameNT 
       | varNameNT '[' expressionNT ']' 
       | subroutineCallNT 
       | '(' expressionNT ')' 
       | unaryOpNT termNT 
       ;

subroutineCallNT : subroutineNameNT '(' expressionListNT ')'
                | (classNameNT|varNameNT) '.' subroutineNameNT '(' expressionListNT ')'
                ;

expressionListNT : (expressionNT (',' expressionNT)*)? ;

opNT : '+'|'-'|'*'|'/'|'&'|'|'|'<'|'>'|'=' ;

unaryOpNT : '-'|'~' ;

keywordConstantNT : 'true'|'false'|'null'|'this' ;

/**
    Lexer rules
 */

INTEGERCONSTANT : [0-9]+ ;

STRINGCONSTANT : '"'~["\n]*'"' ;

IDENTIFIER : [A-Za-z_][A-Za-z0-9_]* ;

WHITESPACE : [ \t\n\r]+ -> skip ;
INLINECOMENT : '//'~[\r\n]* -> skip ;
DOCCOMENT : '/*'.*? '*/' -> skip ;