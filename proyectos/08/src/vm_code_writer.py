"""
Python module containing the CodeWriter class for the VM Translator of the Hack Platform.

Author: Rafael Villegas
"""

class CodeWriter:
  """ Class that translates the VM commands into Hack assembly code """

  def __init__(self, output_file):
    """ 
    Constructor.
    Opens the output file and gets ready to parse it.
    """
    final_output_file = output_file + ".asm"
    self.file = open(final_output_file, 'w+')
    self.current_file = None
    self.current_command_number = 0

  def set_file_name(self, file_name):
    """ Informs the code writer that the translation of a new VM file started """
    self.current_file = file_name

  def write_arithmetic(self, command):
    """ Writes the assembly code corresponding to the given arithmetic command """
    # create empty list to store all the assembly commands
    assembly_commands = []
    
    if command == "add":
      assembly_commands.append("@SP")
      assembly_commands.append("AM=M-1")
      assembly_commands.append("D=M")
      assembly_commands.append("A=A-1")
      assembly_commands.append("M=D+M")
    
    elif command == "sub":
      assembly_commands.append("@SP")
      assembly_commands.append("AM=M-1")
      assembly_commands.append("D=M")
      assembly_commands.append("A=A-1")
      assembly_commands.append("M=M-D")

    elif command == "neg":
      assembly_commands.append("@SP")
      assembly_commands.append("A=M-1")
      assembly_commands.append("M=-M")

    elif command == "eq":
      assembly_commands.append("@SP")
      assembly_commands.append("AM=M-1")
      assembly_commands.append("D=M")
      assembly_commands.append("A=A-1")
      assembly_commands.append("D=M-D")
      assembly_commands.append("@FALSE{}".format(self.current_command_number))
      assembly_commands.append("D;JNE")  # inverse logic
      assembly_commands.append("@SP")
      assembly_commands.append("A=M-1")
      assembly_commands.append("M=-1")
      assembly_commands.append("@END{}".format(self.current_command_number))
      assembly_commands.append("0;JMP")
      assembly_commands.append("(FALSE{})".format(self.current_command_number))
      assembly_commands.append("@SP")
      assembly_commands.append("A=M-1")
      assembly_commands.append("M=0")
      assembly_commands.append("(END{})".format(self.current_command_number))

      self.current_command_number += 1

    elif command == "gt":
      assembly_commands.append("@SP")
      assembly_commands.append("AM=M-1")
      assembly_commands.append("D=M")
      assembly_commands.append("A=A-1")
      assembly_commands.append("D=M-D")
      assembly_commands.append("@FALSE{}".format(self.current_command_number))
      assembly_commands.append("D;JLE")  # inverse logic
      assembly_commands.append("@SP")
      assembly_commands.append("A=M-1")
      assembly_commands.append("M=-1")
      assembly_commands.append("@END{}".format(self.current_command_number))
      assembly_commands.append("0;JMP")
      assembly_commands.append("(FALSE{})".format(self.current_command_number))
      assembly_commands.append("@SP")
      assembly_commands.append("A=M-1")
      assembly_commands.append("M=0")
      assembly_commands.append("(END{})".format(self.current_command_number))

      self.current_command_number += 1

    elif command == "lt":
      assembly_commands.append("@SP")
      assembly_commands.append("AM=M-1")
      assembly_commands.append("D=M")
      assembly_commands.append("A=A-1")
      assembly_commands.append("D=M-D")
      assembly_commands.append("@FALSE{}".format(self.current_command_number))
      assembly_commands.append("D;JGE")  # inverse logic
      assembly_commands.append("@SP")
      assembly_commands.append("A=M-1")
      assembly_commands.append("M=-1")
      assembly_commands.append("@END{}".format(self.current_command_number))
      assembly_commands.append("0;JMP")
      assembly_commands.append("(FALSE{})".format(self.current_command_number))
      assembly_commands.append("@SP")
      assembly_commands.append("A=M-1")
      assembly_commands.append("M=0")
      assembly_commands.append("(END{})".format(self.current_command_number))

      self.current_command_number += 1

    elif command == "and":
      assembly_commands.append("@SP")
      assembly_commands.append("AM=M-1")
      assembly_commands.append("D=M")
      assembly_commands.append("A=A-1")
      assembly_commands.append("M=D&M")

    elif command == "or":
      assembly_commands.append("@SP")
      assembly_commands.append("AM=M-1")
      assembly_commands.append("D=M")
      assembly_commands.append("A=A-1")
      assembly_commands.append("M=D|M")

    elif command == "not":
      assembly_commands.append("@SP")
      assembly_commands.append("A=M-1")
      assembly_commands.append("M=!M")

    # add the newline character to every single command and write them
    for line in assembly_commands:
      self.file.write(line + '\n')

  def write_push_pop(self, command, segment, index):
    """ Writes the assembly code corresponding to the given push or pop command """
    # create an empty list to store all the assembly commands
    assembly_commands = []

    # get the memory segments that behave in the same way into one variable
    asm_seg = ""

    if segment == "argument":
      asm_seg = "ARG"
    elif segment == "local":
      asm_seg = "LCL"
    elif segment == "this":
      asm_seg = "THIS"
    elif segment == "that":
      asm_seg = "THAT"

    if segment == "argument" or segment == "local" or segment == "this" or segment == "that":
      if command == "C_PUSH":
        assembly_commands.append("@{}".format(asm_seg))
        assembly_commands.append("D=M")
        assembly_commands.append("@{}".format(index))
        assembly_commands.append("A=D+A")
        assembly_commands.append("D=M")
        assembly_commands.append("@SP")
        assembly_commands.append("A=M")
        assembly_commands.append("M=D")
        assembly_commands.append("@SP")
        assembly_commands.append("M=M+1")

      elif command == "C_POP":
        assembly_commands.append("@{}".format(asm_seg))
        assembly_commands.append("D=M")
        assembly_commands.append("@{}".format(index))
        assembly_commands.append("D=D+A")
        assembly_commands.append("@R13")
        assembly_commands.append("M=D")
        assembly_commands.append("@SP")
        assembly_commands.append("AM=M-1")
        assembly_commands.append("D=M")
        assembly_commands.append("@R13")
        assembly_commands.append("A=M")
        assembly_commands.append("M=D")

    elif segment == "static":
      if command == "C_PUSH":
        assembly_commands.append("@{}".format(16 + index))
        assembly_commands.append("D=M")
        assembly_commands.append("@SP")
        assembly_commands.append("A=M")
        assembly_commands.append("M=D")
        assembly_commands.append("@SP")
        assembly_commands.append("M=M+1")

      elif command == "C_POP":
        assembly_commands.append("@SP")
        assembly_commands.append("AM=M-1")
        assembly_commands.append("D=M")
        assembly_commands.append("@{}".format(16 + index))
        assembly_commands.append("M=D")

    elif segment == "constant":
      if command == "C_PUSH":
        assembly_commands.append("@{}".format(index))
        assembly_commands.append("D=A")
        assembly_commands.append("@SP")
        assembly_commands.append("A=M")
        assembly_commands.append("M=D")
        assembly_commands.append("@SP")
        assembly_commands.append("M=M+1")

      elif command == "C_POP":
        print("ERROR: Cannot pop into a constant")
        exit(-1)
    
    elif segment == "pointer":
      if command == "C_PUSH":
        assembly_commands.append("@{}".format(3 + index))
        assembly_commands.append("D=M")
        assembly_commands.append("@SP")
        assembly_commands.append("A=M")
        assembly_commands.append("M=D")
        assembly_commands.append("@SP")
        assembly_commands.append("M=M+1")

      elif command == "C_POP":
        assembly_commands.append("@SP")
        assembly_commands.append("AM=M-1")
        assembly_commands.append("D=M")
        assembly_commands.append("@{}".format(3 + index))
        assembly_commands.append("M=D")

    elif segment == "temp":
      if command == "C_PUSH":
        assembly_commands.append("@{}".format(5 + index))
        assembly_commands.append("D=M")
        assembly_commands.append("@SP")
        assembly_commands.append("A=M")
        assembly_commands.append("M=D")
        assembly_commands.append("@SP")
        assembly_commands.append("M=M+1")

      elif command == "C_POP":
        assembly_commands.append("@SP")
        assembly_commands.append("AM=M-1")
        assembly_commands.append("D=M")
        assembly_commands.append("@{}".format(5 + index))
        assembly_commands.append("M=D")

    # add the newline character to every single command and write them
    for line in assembly_commands:
      self.file.write(line + '\n')

  def write_label(self, label):
    """ Writes the assembly code for the specified label """
    self.file.write("({})\n".format(label.upper()))

  def write_goto(self, label):
    """ Writes the assembly command for the given goto vm command """
    self.file.write("@{}\n".format(label.upper()))
    self.file.write("0;JMP\n")

  def write_if(self, label):
    """ Writes the assembly command for the given if-goto vm command """
    # create an empty list to store all the asm commands
    assembly_commands = []

    # add the commands the list
    assembly_commands.append("@SP")
    assembly_commands.append("AM=M-1")
    assembly_commands.append("D=M")
    assembly_commands.append("@{}".format(label.upper()))
    assembly_commands.append("D;JNE")

    # write the commands to the output file
    for line in assembly_commands:
      self.file.write(line + '\n')

  
  def close(self):
    """ Closes the output file associated to the object """
    self.file.close()
    
# cw = CodeWriter("test.asm")
# cw.write_push_pop("C_PUSH", "pointer", 0)
# cw.close()