#!/usr/bin/env python3
""" 
Main module of the VM Translator for the Hack platform.

It uses the Parser and CodeWriter classes to read a Jack VM language file (.vm)
and generates a Hack assembly file (.asm)

Author: Rafael Villegas
"""

import sys

from vm_parser import Parser
from vm_code_writer import CodeWriter

def main():
  """ 
  Starts the translation from VM language to Hack assembly 
  by marching line by line in a .vm file 
  """

  if len(sys.argv) != 2 or sys.argv[1][-3:] != ".vm":
    bad_usage()

  # get the name of the vm file to be parsed
  input_file_name = str(sys.argv[1])
  # create parser and code writer
  parser = Parser(input_file_name)
  code_writer = CodeWriter(input_file_name[0:-3])
  
  # while there are more commands, keep advancing
  while parser.has_more_commands():
    parser.advance()
    # HANDLE ARITHMETIC COMMANDS
    if parser.command_type() == "C_ARITHMETIC":
      # get the command
      command = parser.arg1()
      # write it's corresponding assembler commands to the output
      code_writer.write_arithmetic(command)
    
    # HANDLE PUSH AND POP COMMANDS
    elif parser.command_type() == "C_PUSH" or parser.command_type() == "C_POP":
      # get the memory segment and the index
      mem_segment = parser.arg1()
      index = parser.arg2()
      # write it's assembler commands to the output
      code_writer.write_push_pop(parser.command_type(), mem_segment, index)

    # HANDLE LABEL COMMANDS
    elif parser.command_type() == "C_LABEL":
      # get the command
      label = parser.arg1()
      # write it's corresponding assembler commands to the output
      code_writer.write_label(label)

    # HANDLE GOTO COMMANDS
    elif parser.command_type() == "C_GOTO":
      # get the command
      label = parser.arg1()
      # write it's corresponding assembler commands to the output
      code_writer.write_goto(label)

    # HANDLE IF COMMANDS
    elif parser.command_type() == "C_IF":
      # get the command
      label = parser.arg1()
      # write it's corresponding assembler commands to the output
      code_writer.write_if(label)

  del parser
  code_writer.close()


def bad_usage():
  """ Funtion that manages a bad argument usage of the program, terminating it right away """
  
  print("Usage: python3 vm_translator.py <File Name>.vm")
  sys.exit(-1)

if __name__ == "__main__":
  main()