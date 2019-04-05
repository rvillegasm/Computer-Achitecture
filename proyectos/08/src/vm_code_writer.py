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
    self.current_function_name = ""
    self.current_command_number = 0

  def set_file_name(self, file_name):
    """ Informs the code writer that the translation of a new VM file started """
    # split the path to the file name
    file_path = file_name.split("/")
    # get the last part, which is the name of the actual file
    file = file_path[-1]
    # set it
    self.current_file = file

  def set_function_name(self, function_name):
    """ Informs the code writer that the translation of a new VM function started """
    self.current_function_name = function_name

  def write_init(self):
    """ Writes the assembly code for the VM initialization (bootstrap code). """

    self.set_file_name("Sys")

    # add the commands
    # SP = 256
    self.file.write("@256\n")
    self.file.write("D=A\n")
    self.file.write("@SP\n")
    self.file.write("M=D\n")
    # call Sys.init
    self.write_call("Sys.init", 0)

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
    self.file.write("({}.{}:{})\n".format(self.current_file.upper(), self.current_function_name.upper(), label.upper()))

  def write_goto(self, label):
    """ Writes the assembly command for the given goto vm command """
    self.file.write("@{}.{}:{}\n".format(self.current_file.upper(), self.current_function_name.upper(), label.upper()))
    self.file.write("0;JMP\n")

  def write_if(self, label):
    """ Writes the assembly command for the given if-goto vm command """
    # create an empty list to store all the asm commands
    assembly_commands = []

    # add the commands the list
    assembly_commands.append("@SP")
    assembly_commands.append("AM=M-1")
    assembly_commands.append("D=M")
    assembly_commands.append("@{}.{}:{}".format(self.current_file.upper(), self.current_function_name.upper(), label.upper()))
    assembly_commands.append("D;JNE")

    # write the commands to the output file
    for line in assembly_commands:
      self.file.write(line + '\n')

  def write_call(self, function_name, num_args):
    """ Writes the assembly command for the given call vm command """
    
    # set the function name to the current function
    self.set_function_name(function_name)
    # create an empty list to store all the asm commands
    assembly_commands = []

    # add the commands to the list 
    # push the return address
    assembly_commands.append("@{}.{}_RETURN".format(self.current_file.upper(), self.current_function_name.upper()))
    assembly_commands.append("D=A")                                                                                           
    assembly_commands.append("@SP")
    assembly_commands.append("A=M")
    assembly_commands.append("M=D")
    assembly_commands.append("@SP")
    assembly_commands.append("M=M+1")
    # push LCL
    assembly_commands.append("@LCL")
    assembly_commands.append("D=M")
    assembly_commands.append("@SP")
    assembly_commands.append("A=M")
    assembly_commands.append("M=D")
    assembly_commands.append("@SP")
    assembly_commands.append("M=M+1")
    # push ARG
    assembly_commands.append("@ARG")
    assembly_commands.append("D=M")
    assembly_commands.append("@SP")
    assembly_commands.append("A=M")
    assembly_commands.append("M=D")
    assembly_commands.append("@SP")
    assembly_commands.append("M=M+1")
    # push THIS
    assembly_commands.append("@THIS")
    assembly_commands.append("D=M")
    assembly_commands.append("@SP")
    assembly_commands.append("A=M")
    assembly_commands.append("M=D")
    assembly_commands.append("@SP")
    assembly_commands.append("M=M+1")
    # push THAT
    assembly_commands.append("@THAT")
    assembly_commands.append("D=M")
    assembly_commands.append("@SP")
    assembly_commands.append("A=M")
    assembly_commands.append("M=D")
    assembly_commands.append("@SP")
    assembly_commands.append("M=M+1")
    # ARG = SP - num_args - 5
    assembly_commands.append("@SP")                                                 #TODO: da diferentes errores con y sin, pero estructura es igual.
    assembly_commands.append("D=M")
    assembly_commands.append("@{}".format(num_args))
    assembly_commands.append("D=D-A")
    assembly_commands.append("@5")
    assembly_commands.append("D=D-A")
    assembly_commands.append("@ARG")
    assembly_commands.append("M=D")
    # LCL = SP
    assembly_commands.append("@SP")
    assembly_commands.append("D=M")
    assembly_commands.append("@LCL")
    assembly_commands.append("M=D")
    # goto func
    assembly_commands.append("@{}.{}".format(self.current_file.upper(), self.current_function_name.upper()))
    assembly_commands.append("0;JMP")
    # return address label
    assembly_commands.append("({}.{}_RETURN)".format(self.current_file.upper(), self.current_function_name.upper()))

    # write the commands to the output file
    for line in assembly_commands:
      self.file.write(line + '\n')

  def write_return(self):
    """ Writes the assembly command for the given return vm command """
    # create an empty list to store the asm commands
    assembly_commands = []
    
    # add the commands 
    # FRAME = LCL
    assembly_commands.append("@LCL")
    assembly_commands.append("D=M")
    assembly_commands.append("@R14")
    assembly_commands.append("M=D")
    # RET = *(FRAME - 5)
    assembly_commands.append("@5")
    assembly_commands.append("A=D-A")
    assembly_commands.append("D=M")
    assembly_commands.append("@R15")
    assembly_commands.append("M=D")
    # *ARG = pop()
    assembly_commands.append("@SP")
    assembly_commands.append("AM=M-1")
    assembly_commands.append("D=M")
    assembly_commands.append("@ARG")
    assembly_commands.append("A=M")
    assembly_commands.append("M=D")
    # SP = ARG + 1
    assembly_commands.append("@ARG")
    assembly_commands.append("D=M+1")
    assembly_commands.append("@SP")
    assembly_commands.append("M=D")
    # THAT = *(FRAME-1)
    assembly_commands.append("@R14")
    assembly_commands.append("A=M-1")
    assembly_commands.append("D=M")
    assembly_commands.append("@THAT")
    assembly_commands.append("M=D")
    # THIS = *(FRAME-2)
    assembly_commands.append("@R14")
    assembly_commands.append("D=M")
    assembly_commands.append("@2")
    assembly_commands.append("A=D-A")
    assembly_commands.append("D=M")
    assembly_commands.append("@THIS")
    assembly_commands.append("M=D")
    # ARG = *(FRAME-3)
    assembly_commands.append("@R14")
    assembly_commands.append("D=M")
    assembly_commands.append("@3")
    assembly_commands.append("A=D-A")
    assembly_commands.append("D=M")
    assembly_commands.append("@ARG")
    assembly_commands.append("M=D")
    # LCL = *(FRAME-4)
    assembly_commands.append("@R14")
    assembly_commands.append("D=M")
    assembly_commands.append("@4")
    assembly_commands.append("A=D-A")
    assembly_commands.append("D=M")
    assembly_commands.append("@LCL")
    assembly_commands.append("M=D")
    # goto RET
    assembly_commands.append("@R15")
    assembly_commands.append("A=M")
    assembly_commands.append("0;JMP")
  
    # write the commands to the output file
    for line in assembly_commands:
      self.file.write(line + '\n')

  def write_function(self, function_name, num_locals):
    """ Writes the assembly command for the given function vm command """
    # create an empty list to store the asm commands
    assembly_commands = []

    # add the asm commands
    # (func)
    assembly_commands.append("({}.{})".format(self.current_file.upper(), function_name.upper()))
    # push 0 for every local variable
    for _ in range(num_locals):
      assembly_commands.append("@SP")
      assembly_commands.append("A=M")
      assembly_commands.append("M=0")
      assembly_commands.append("@SP")
      assembly_commands.append("M=M+1")

    # write the commands to the output file
    for line in assembly_commands:
      self.file.write(line + '\n')

  
  def close(self):
    """ Closes the output file associated to the object """
    self.file.close()
    
# cw = CodeWriter("test.asm")
# cw.write_push_pop("C_PUSH", "pointer", 0)
# cw.close()