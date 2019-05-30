"""
Module containing an Error Listener implementation for the Jack Compiler.
It is based on the ANTLR4 runtime.
"""

from antlr4.error.ErrorListener import ErrorListener

class ErrorHandler(ErrorListener):
    """ Class containing an alternative error listener implementation to the one built into the ANTLR4 runtime """
    
    def __init__(self):
        super(ErrorHandler, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError("Syntax Error!: Unrecognized token '{}' in line: {} and column: {}".format(offendingSymbol.text, line, column))