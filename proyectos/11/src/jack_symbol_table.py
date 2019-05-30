"""
Module containing the symbol table class for the jack compiler.
"""

class SymbolTable:
    """
    A symbol table that associates names with information needed for Jack compilation: 
    type, kind, and running index.

    The symbol table has 2 nested scopes (class/subroutine).
    """

    def __init__(self):
        """ 
        Creates a new Symbol Table with class and subroutine scopes.
        Each scope is a dictionary of lists, in which every entry is the name of the symbol 
        and the value is a list o it's type, kind and number (in that order).
        """
        self.symbol_table = {
                                "class": {},
                                "subroutine": {}
                            }
        self.static_index = 0
        self.field_index = 0 
        self.arg_index = 0 
        self.var_index = 0

    def start_subroutine(self):
        """ Starts a new subroutine scope, erasing everything from the last subroutine scope."""
        self.symbol_table["subroutine"] = {}
        self.arg_index = 0
        self.var_index = 0

    def define(self, symbol_name, symbol_type, symbol_kind):
        """ 
        Defines a new identifier of a given name, type, and kind and assigns it a running index.
        STATIC and FIELD identifiers have a class scope, 
        while ARG and VAR identifiers have a subroutine scope.
        """
        if symbol_kind == "STATIC":
            self.symbol_table["class"][symbol_name] = [symbol_type, symbol_kind, self.static_index]
            self.static_index += 1

        elif symbol_kind == "FIELD":
            self.symbol_table["class"][symbol_name] = [symbol_type, symbol_kind, self.field_index]
            self.field_index += 1

        elif symbol_kind == "ARG":
            self.symbol_table["subroutine"][symbol_name] = [symbol_type, symbol_kind, self.arg_index]
            self.arg_index += 1

        elif symbol_kind == "VAR":
            self.symbol_table["subroutine"][symbol_name] = [symbol_type, symbol_kind, self.var_index]
            self.var_index += 1

    def var_count(self, kind):
        """ Returns the number of variables of the given kind already defined in the current scope. """
        if kind == "STATIC":
            return self.static_index
        elif kind == "FIELD":
            return self.field_index
        elif kind == "ARG":
            return self.arg_index
        elif kind == "VAR":
            return self.var_index
    
    def kind_of(self, name):
        """
        Returns the kind of the named identifier in the current scope. 
        Returns 'None' if the identifier is unknown in the current scope.
        """
        if name in self.symbol_table["subroutine"]:
            return self.symbol_table["subroutine"][name][1]
            
        elif name in self.symbol_table["class"]:
            return self.symbol_table["class"][name][1]

        else:
            return None

    def type_of(self, name):
        """ Returns the type of the named identifier in the current scope. """
        if name in self.symbol_table["subroutine"]:
            return self.symbol_table["subroutine"][name][0]
            
        elif name in self.symbol_table["class"]:
            return self.symbol_table["class"][name][0]

        else:
            return None

    def index_of(self, name):
        """ Returns the index assigned to named identifier. """
        if name in self.symbol_table["subroutine"]:
            return self.symbol_table["subroutine"][name][2]
            
        elif name in self.symbol_table["class"]:
            return self.symbol_table["class"][name][2]

        else:
            return None
        
# table = SymbolTable()
# table.define("HELLO", 'STRING', 'ARG')
# table.define("aaa", 'int', 'ARG')
# table.define("HELLO", 'STRING', 'STATIC')
# kind = table.kind_of("aaa")
# typeof = table.type_of("aaa")
# index = table.index_of("aaa")
# print(table.symbol_table, '\n')
# print(kind, typeof, index)