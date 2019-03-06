"""
Python module containing the SymbolTable class for the hack assembler.

Author: Rafael Villegas
"""

class SymbolTable:
  """ 
  Keeps correspondence between symbols and their numeric address.

  Attributes:
  -----------
  symbol_map : dict
    symbol table that contains all the memory addres values for every symbol in a program
  """

  def __init__(self):
    """ Initializes the symbol table with all the pre-defined symbols """
    self.symbol_map = {
                       "R0": 0,
                       "R1": 1,
                       "R2": 2,
                       "R3": 3,
                       "R4": 4,
                       "R5": 5,
                       "R6": 6,
                       "R7": 7,
                       "R8": 8,
                       "R9": 9,
                       "R10": 10,
                       "R11": 11,
                       "R12": 12,
                       "R13": 13,
                       "R14": 14,
                       "R15": 15,
                       "SP": 0,
                       "LCL": 1,
                       "ARG": 2,
                       "THIS": 3,
                       "THAT": 4,
                       "SCREEN": 16384,
                       "KBD": 24576
                      }

  def addEntry(self, symbol, address):
    """ Adds a new symbol to the table, with the specified address """
    self.symbol_map[symbol] = address

  def contains(self, symbol):
    """ Returns True if the symbol is already in the table """
    return symbol in self.symbol_map

  def get_address(self, symbol):
    """ Returns the address of a symbol already in the table """
    return self.symbol_map[symbol]
    