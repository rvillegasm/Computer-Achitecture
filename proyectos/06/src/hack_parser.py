"""
Python module containing the Parser class for the Hack assembler.

Author: Rafael Villegas
"""

class Parser:
  """
  Class that reads the assembler source file, parses it and provides acces to it's fields and symbols.
  It encapsulates the access to the source file.
  
  Attributes:
  -----------
  file : obj
    File to be parsed

  current_command : str
    command to be analysed
  """

  def __init__(self, source_file):
    """ 
    Constructor.
    Recieves a file to be parsed and opens it.
    """
    self.file = open(source_file, "r")
    self.current_command = None

  def __del__(self):
    """
    Destructor.
    Closes the file that was opened by the contructor.
    """
    self.file.close()

  def has_more_commands(self):
    """ 
    Evaluates if there is still a new command left to parse.
    Returns bool and the line to be parsed.
    """
    # peeks into the next line
    next_line = self._peek_next_line()

    # if it is a comment line, ignore it and read the next one until you find one that is not a comment.
    # same with the empty lines (lines that are composed only of the \n charachter)
    while next_line.strip()[0:2] == "//" or next_line == "\n":
      # read the comment line and ignore it (peek into the next line)
      next_line = self.file.readline()
      next_line = self._peek_next_line()

    if next_line is not "":
      return True
    
    return False

  def advance(self):
    """ Reads the next line, ignoring the leading and trailing whitespaces, making it the current command """
    self.current_command = self.file.readline().strip()

  def command_type(self):
    """ Returns type of current command (A, C, or L) """
    command = self.current_command
    
    # try to find a comment
    comment_index = command.find("//")
    # if a comment is found, ignore it and also update the class attribute  
    if comment_index != -1:
      command = command[0:comment_index].strip()
      self.current_command = command
    
    # if it starts with an @, it is of type A
    if command[0] == '@' and command[1:] != "":
      return "A_COMMAND"
    # if it has an = or a ;, it is of type C
    elif ('=' in command or ';' in command):
      return "C_COMMAND"
    # if it has a set of parenthesys, it is of type L
    elif command[0] == '(' and command[-1] == ')' and command[1:-1].strip() != "":
      return "L_COMMAND"
    # if none of the above, throw a Syntax error
    else:
      print("ERROR: command [{}] is not a valid command!\n".format(command))
      raise SyntaxError

  def symbol(self):
    """ Returns the symbol xxx in @xxx or (xxx) """
    command = self.current_command
    
    if command[0] == '@':
      return command[1:]

    elif command[0] == '(' and command[-1] == ')':
      return command[1:-1]

  def dest(self):
    """ Returns the dest mnemonic in dest=comp;jump. If there isn't a dest, it returns None """
    command = self.current_command
    
    if '=' in command:
      equal_index = command.find('=')
      return command[0:equal_index]

    else:
      return None

  def comp(self):
    """ Returns the comp mnemonic in dest=comp;jump """
    command = self.current_command

    # if the command has both dest and jump, comp will be between '=' and ';'
    if '=' in command and ';' in command:
      equal_index = command.find('=')
      semicolon_index = command.find(';')
      return command[equal_index+1:semicolon_index]
    # if the command has only dest and not jump, comp wil be after '='
    elif '=' in command:
      equal_index = command.find('=')
      return command[equal_index+1:]
    # if the command has only jump and not dest, comp will be before ';'
    elif ';' in command:
      semicolon_index = command.find(';')
      return command[:semicolon_index]

  def jump(self):
    """ Returns the jump mnemonic in dest=comp;jump. If there isn't a jump, it returns None """
    command = self.current_command

    if ';' in command:
      semicolon_index = command.find(';')
      return command[semicolon_index+1:]

    else:
      return None
    
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
