"""
Python module containing the Code class for the Hack assembler.

Author: Rafael Villegas
"""

class Code:
  """ 
  Class that translates hack assembly language mnemonics into their binary representation.

  Static Attributes:
  ------------------
  dest_table : dict
    Relations between dest mnemonics and their binary values
  jummp_table : dict
    Relations between jump mnemonics and their binary values
  comp_table : dict
    Relations between comp mnemonics and their binary values
  """

  """ Map containing the relations between dest mnemonics and their binary value """
  dest_table = {
                 None: "000",
                  "M": "001",
                  "D": "010",
                 "MD": "011",
                  "A": "100",
                 "AM": "101",
                 "AD": "110",
                "AMD": "111"
                }

  """ Map containing the relations between jump mnemonics and their binary value """
  jump_table = {
                 None: "000",
                "JGT": "001",
                "JEQ": "010",
                "JGE": "011",
                "JLT": "100",
                "JNE": "101",
                "JLE": "110",
                "JMP": "111"
               }

  """ Map containing the relations between comp mnemonics and their binary value"""
  comp_table = {
                  "0": "0101010",
                  "1": "0111111",
                 "-1": "0111010",
                  "D": "0001100",
                  "A": "0110000",
                 "!D": "0001101",
                 "!A": "0110001",
                 "-D": "0001111",
                 "-A": "0110011",
                "D+1": "0011111",
                "A+1": "0110111",
                "D-1": "0001110",
                "A-1": "0110010",
                "D+A": "0000010",
                "D-A": "0010011",
                "A-D": "0000111",
                "D&A": "0000000",
                "D|A": "0010101",
                  "M": "1110000",
                 "!M": "1110001",
                 "-M": "1110011",
                "M+1": "1110111",
                "M-1": "1110010",
                "D+M": "1000010",
                "D-M": "1010011",
                "M-D": "1000111",
                "D&M": "1000000",
                "D|M": "1010101"
               }

  def dest(self, mnemonic):
    """ Returns the binary value of a dest mnemonic. If it is not found, a Syntax Error is thrown """

    if mnemonic in Code.dest_table:
      return Code.dest_table[mnemonic]
    else:
      print("ERROR: mnemonic [{}] is not a valid dest expression!\n".format(mnemonic))
      raise SyntaxError

  def comp(self, mnemonic):
    """ Returns the binary value of a comp mnemonic. If it is not found, a Syntax Error is thrown """

    if mnemonic in Code.comp_table:
      return Code.comp_table[mnemonic]
    else:
      print("ERROR: mnemonic [{}] is not a valid comp expression!\n".format(mnemonic))
      raise SyntaxError

  def jump(self, mnemonic):
    """ Returns the binary value of a jump mnemonic. If it is not found, a Syntax Error is thrown """

    if mnemonic in Code.jump_table:
      return Code.jump_table[mnemonic]
    else:
      print("ERROR: mnemonic [{}] is not a valid jump expression!\n".format(mnemonic))
      raise SyntaxError