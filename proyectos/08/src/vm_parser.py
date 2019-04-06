"""
Python module containing the Parser class for the VM Translator of the Hack Platform.

Author: Rafael Villegas
"""

class Parser:
  """
  Class that handels the parsing of a single .vm file, and enapsulates acces to the input code.
  It reads VM commands, parses them, and provides acces to their components.
  """

  # Static class variable containing the arithmetic and logic commands
  arithmetic_and_logic_commands = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]
  # Static class variable containing the memory segments
  memory_segments = ["argument", "local", "static", "constant", "this", "that", "pointer", "temp"]

  def __init__(self, source_file):
    """
    Constructor.
    Opens the input file and gets ready to parse it. 
    """
    self.file = open(source_file, 'r')
    self.current_command = None

  def __del__(self):
    """
    Destructor.
    Closes the source file associated to the object. 
    """
    self.file.close()

  def has_more_commands(self):
    """ 
    Evaluates if there is still a new command left to parse.
    Returns bool.
    """
    # get the next line
    next_line = self._peek_next_line()

    # if it is a comment line, ignore it and read the next one until you find one that is not a comment.
    # same with the empty lines (lines that are composed only of the \n charachter)
    while next_line.strip()[0:2] == "//" or next_line == "\n":
      # read the comment line and ignore it (peek into the next line)
      next_line = self.file.readline()
      next_line = self._peek_next_line()

    # if the next line is not an empty string, then there is another command left to be parsed
    if next_line is not "":
      return True
    # if the next line is an empty string, there are no commands left to be parsed
    return False

  def advance(self):
    """ Reads the next line, ignoring the leading and trailing whitespaces, making it the current command """
    self.current_command = self.file.readline().strip()

  def command_type(self):
    """
    Returns type of current VM command. 
    Values can be C_ARITHMETIC, C_PUSH, C_POP.
    """
  
    command = self.current_command
    
    # checks if there is a comment in the current command
    # if it finds one, the index will be different from -1
    comment_index = command.find("//")
    # if a comment is found, ignore it and also update the class attribute
    if comment_index != -1:
      command = command[0:comment_index].strip()
      self.current_command = command

    # slpit the command into it's underlying components
    command_components = command.split(" ")

    # if the first component is and arithmetic or logic command, return C_ARITHMETIC
    if command_components[0] in Parser.arithmetic_and_logic_commands:
      return "C_ARITHMETIC"
    # else, if it is push, return C_PUSH
    elif command_components[0] == "push":
      return "C_PUSH"
    # else, if it is pop, return C_POP
    elif command_components[0] == "pop":
      return "C_POP"
    # else, if it is label, return C_LABEL
    elif command_components[0] == "label":
      return "C_LABEL"
    # else, if it is goto, return C_GOTO
    elif command_components[0] == "goto":
      return "C_GOTO"
    # else, if it is if-goto, return C_IF
    elif command_components[0] == "if-goto":
      return "C_IF"
    # else, if it is function, return C_FUNCTION
    elif command_components[0] == "function":
      return "C_FUNCTION"
    # else, if it is call, return C_CALL
    elif command_components[0] == "call":
      return "C_CALL"
    # else, if it is return, return C_RETURN
    elif command_components[0] == "return":
      return "C_RETURN"
    
    else:
      print("ERROR: Command [{}] is not a valid command!".format(command_components[0]))
      exit(-1)

  def arg1(self):
    """ 
    Returns the first argument of the current command, 
    or the command itself in the case of C_ARITHMETIC 
    """
    # get the components of the current command
    command = self.current_command
    command_components = command.split()

    # if the current command is an arithmetic command, return the command itself
    if self.command_type() == "C_ARITHMETIC":
      return command_components[0]
    # else, it is a push por a pop command, in which case we try to return the first argument
    elif self.command_type() == "C_PUSH" or self.command_type() == "C_POP":
      try:
        # if the argument is not a valid memory segment, throw an error
        if command_components[1] in Parser.memory_segments:
          return command_components[1]
        else:
          print("ERROR: argument [{}] is not a memory segment".format(command_components[1]))
          exit(-1)
      # catch the argument index error    
      except IndexError:
        print("ERROR: Missing an argument for the command [{}]!".format(command))
        exit(-1)
    # if it is not a push or pop command, check if it is a goto, label, if, function or call command
    elif self.command_type() == "C_LABEL" or self.command_type() == "C_GOTO" or self.command_type() == "C_IF" or self.command_type() == "C_FUNCTION" or self.command_type() == "C_CALL":
      try:
        return command_components[1]
      except IndexError:
        print("ERROR: Missing a label argument for the command [{}]!".format(command))
        exit(-1)

  def arg2(self):
    """ 
    Returns the second argument of the current command.
    Call it only when command type is C_PUSH, C_POP, C_FUNCTION, C_CALL, C_FUNCTION, C_CALL 
    """

    # get the current command
    command = self.current_command
    # try to get the second argument of the command
    try:
      second_argument = command.split(" ")[2]
    # if there isn't a second argument, throw an error
    except IndexError:
      print("ERROR: Missing an argument for the command [{}]!".format(command))
      exit(-1)
    # if the second argument is not a number, throw an error
    if second_argument.isnumeric():
      return int(second_argument)
    else:
      print("ERROR: Argument [{}] is not a valid argument!".format(second_argument))
      exit(-1)

  # HELPER FUNCTION
  def _peek_next_line(self):
    """ 
    Helper method that is used to see the contents of a line "without actually reading it",
    so it can be read again later.
    """
    # get the current line position on the file
    position = self.file.tell()
    # read the next line
    next_line = self.file.readline()
    # go back to the previous position
    self.file.seek(position)
    # return the line that was read
    return next_line


# p = Parser("test.txt")
# while p.has_more_commands():
#   p.advance()
#   if p.command_type() == "C_ARITHMETIC":
#     print(p.arg1())
#   elif p.command_type() == "C_PUSH":
#     print(p.arg1() + p.arg2())
#   elif p.command_type() == "C_POP":
#     print(p.arg1() + p.arg2())