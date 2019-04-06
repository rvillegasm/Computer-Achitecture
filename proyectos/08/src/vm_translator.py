#!/usr/bin/env python3
""" 
Main module of the VM Translator for the Hack platform.

It uses the Parser and CodeWriter classes to read a Jack VM language file (.vm)
and generates a Hack assembly file (.asm)

Author: Rafael Villegas
"""

import os
import sys

from vm_parser import Parser
from vm_code_writer import CodeWriter

def main():
  """ 
  Starts the translation from VM language to Hack assembly 
  by marching line by line in a .vm file 
  """

  if not os.path.isdir(sys.argv[1]) and (len(sys.argv) != 2 or sys.argv[1][-3:] != ".vm"):
    bad_usage()

  code_writer = None

  if os.path.isdir(sys.argv[1]):
    # create the code writer
    # there is only one for the whole translation
    file_path = sys.argv[1].split("/")
    if file_path[-1] != "":
      code_writer = CodeWriter("{}/{}".format(sys.argv[1], file_path[-1]))
    else:
      code_writer = CodeWriter("{}/{}".format(sys.argv[1], file_path[-2]))

    translate_directory(sys.argv[1], code_writer)
  else:
    code_writer = CodeWriter(sys.argv[0:-3])
    translate_one_file(sys.argv[1], code_writer)

  code_writer.close()


def translate_directory(directory, code_writer):
  """ Translates every VM file inside a direcotry into a single Assembler file """

  # create an empty list to store all the vm files
  vm_files = []
  path = None
  # walk through the files
  for root, _, files in os.walk(directory):
    path = root
    for f in files:
      # check if it is a vm file and add it to the list
      if f.endswith(".vm"):
        # translate_one_file(os.path.join(root, f), code_writer)
        vm_files.append(f)
  
  # parse and translate, depending on the number of files
  if len(vm_files) == 1:
    translate_one_file(os.path.join(path, vm_files[0]), code_writer)
  # if there are more than 2 vm files, initialize it and translate everything
  elif len(vm_files) > 1:
    code_writer.write_init()
    for file in vm_files:
      translate_one_file(os.path.join(path, file), code_writer)
  # if there are no vm files, throw an error
  else:
    print("ERROR: No VM files in the specified directory!")
    sys.exit(-1)


def translate_one_file(input_file_name, code_writer):
  """ Translates just one VM file into an Assembler file """

  # create parser and set the code writer to the current file
  parser = Parser(input_file_name)
  code_writer.set_file_name(input_file_name[0:-3])
  
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

    # HANDLE CALL COMMANDS
    elif parser.command_type() == "C_CALL":
      # get the function name
      function_name = parser.arg1()
      # get the number of arguments
      num_args = parser.arg2()
      # write it's corresponding assembler code to the output
      code_writer.write_call(function_name, num_args)

    # HANDLE RETURN COMMANDS
    elif parser.command_type() == "C_RETURN":
      code_writer.write_return()

    # HANDLE FUNCTION COMMANDS
    elif parser.command_type() == "C_FUNCTION":
      # get the function name
      function_name = parser.arg1()
      # get the number of local variables
      num_local = parser.arg2()
      # write it's corresponding assembler code to the output
      code_writer.write_function(function_name, num_local)

  del parser


def bad_usage():
  """ Funtion that manages a bad argument usage of the program, terminating it right away """
  
  print("Usage: python3 vm_translator.py [<File Name>.vm | <Directory containing at least one .vm file>] ")
  sys.exit(-1)

if __name__ == "__main__":
  main()
