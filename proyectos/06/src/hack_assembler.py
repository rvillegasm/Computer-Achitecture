#!/usr/bin/env python3
""" 
Main module of the Assembler for the Hack platform.

It uses the Parser, Code and SymbolTable classes to read a Hack assembly language source file (.asm)
and generate an executable file (.hack)

It works in three steps:
  * An INITIALIZATION phase, in which the symbol table is generated, as well as the ROM and RAM counters foe symbols.
  * A FIRST PASS in which it reads the file and adds all the lables to the symbol table.
  * A SECOND PASS in which it goes through the source file line by line and translates every command
    to a 16 bit binary value, adding to the symbol table every unknown variable that it encounters.

Author: Rafael Villegas
"""

import sys

from hack_parser import Parser
from hack_code import Code
from hack_symbol_table import SymbolTable

def main():
  """ Executes the Hack Assembler """
  # if there is no source file specified, terminate the program
  if len(sys.argv) != 2:
    bad_usage()

  source_file = str(sys.argv[1])

  # get the name of the file, so it can be used again when writing to the .hack file
  # also, if the file to be parsed isn't a .asm file, terminate the execution
  extention_index = source_file.find('.asm')
  if source_file[extention_index:] != ".asm":
    bad_usage()
    
  file_name = source_file[0:extention_index]

  # initialize symbol table
  symbol_table = SymbolTable()
  # initialize the rom and ram counters for the symbl table
  rom_counter = 0
  ram_counter = 16

  # --------------------------------------------FIRST PASS---------------------------------------------------------
  # create parser
  parser = Parser(source_file)

  # read the whole file
  while parser.has_more_commands():
    parser.advance()
    if parser.command_type() == "L_COMMAND":
      # get the symbol for the label
      label_symbol = parser.symbol()
      # check thtat the label is a valid simbol
      if label_symbol[0].isnumeric():
        print("ERROR: symbol [{}] is not a valid symbol!\n".format(label_symbol))
        raise SyntaxError
      # add the label to the table
      symbol_table.addEntry(label_symbol, rom_counter)
    else:
      # if it finds an A or C instruction, add 1 to the rom counter
      rom_counter += 1
  # delete parser after the first pass, to be able to read the file again
  del parser


  # ---------------------------------------------SECOND PASS-------------------------------------------------------
  # create parser and coder
  parser = Parser(source_file)
  coder = Code()
  # list in which to store all the translated binary commands
  binary_commands = []

  # read the whole file
  while parser.has_more_commands():
    parser.advance()
    # A-Command
    if parser.command_type() == "A_COMMAND":
      # get the symbol
      variable_symbol = parser.symbol()
      # if it is not a number,but rather a variable 
      if not variable_symbol[0].isdigit():
        # if the variable is in the table, get itś addres, translate it to 16-bit binary and add it to the list of commands
        if symbol_table.contains(variable_symbol):
          variable_addres = symbol_table.get_address(variable_symbol)
          binary_variable = "{:016b}".format(variable_addres)
          binary_commands.append(binary_variable+"\n")
        # if it is not in the table, add it and then translate; then add 1 to the ram counter.
        # also add to the binary command list
        else:
          symbol_table.addEntry(variable_symbol, ram_counter)
          binary_variable = "{:016b}".format(ram_counter)
          binary_commands.append(binary_variable+"\n")
          ram_counter += 1
      
      # else if the symbol is a number, just translate it and add it to the list of commands
      elif variable_symbol.isdigit():
        binary_number = "{:016b}".format(int(variable_symbol))
        binary_commands.append(binary_number+"\n")

      else:
        print("ERROR: symbol [{}] is not a valid symbol!\n".format(variable_symbol))
        raise SyntaxError
    
    # C-Command
    elif parser.command_type() == "C_COMMAND":
      # get dest, comp and jump mnemonics of the command
      dest_mnemonic = parser.dest()
      comp_mnemonic = parser.comp()
      jump_mnemonic = parser.jump()
      # get the binary representation of each mnemonic using the coder (Code class)
      binary_dest = coder.dest(dest_mnemonic)
      binary_comp = coder.comp(comp_mnemonic)
      binary_jump = coder.jump(jump_mnemonic)

      # merge the three parts into one, following the structure comp bits -> dest bits -> jump bits 
      full_binary_command = "111{0}{1}{2}".format(binary_comp, binary_dest, binary_jump)
      # add to the list of commands
      binary_commands.append(full_binary_command+"\n")

  # delete parser because it is not needed anymore 
  # also because it opens a file and we need to open another one
  del parser

  # open the corresponding .hack file and write the commands to it, line by line
  with open(file_name + ".hack", "w") as exectuable_file:
    exectuable_file.writelines(binary_commands)

def bad_usage():
  """ Funtion that manages a bad argument usage of the program, terminating it right away """
  
  print("Usage: python3 hack_assembler.py <Source File>.asm")
  sys.exit(-1)


if __name__ == "__main__":
  main()
