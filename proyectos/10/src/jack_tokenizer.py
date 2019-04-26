"""
Module containing the Tokenizer for the Jack Compiler
"""

import re

class Tokenizer:
    """ 
    Class that removes all comments and white spaces from the input stream
    and breaks it into Jack language tokens 
    """

    # static variables representing the regular expressions for the tokens
    KEYWORDS = r"(class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this|let|do|if|else|while|return)"
    SYMBOLS = r"([{}()[\].,;+\-*/&|<>=~])"
    INTEGER_CONSTANTS = r"([0-9]|[1-8][0-9]|9[0-9]|[1-8][0-9]{2}|9[0-8][0-9]|99[0-9]|[1-8][0-9]{3}|9[0-8][0-9]{2}|99[0-8][0-9]|999[0-9]|[12][0-9]{4}|3[01][0-9]{3}|32[0-6][0-9]{2}|327[0-5][0-9]|3276[0-7])"
    STRING_CONSTRANTS = r"\"([^\n]*)\""
    IDENTIFIERS = r"([A-Za-z_]\w*)"
    
    LEXICAL_ELEMENTS = r"{}|{}|{}|{}|{}".format(KEYWORDS, SYMBOLS, INTEGER_CONSTANTS, STRING_CONSTRANTS, IDENTIFIERS)

    MULTILINE_COMMENTS = r"/\*.*?\*/"
    INLINE_COMMENT = r"//.*\n"

    def __init__(self, input_file):
        """ Opens the input file and gets ready to tokenize it """
        self.input_file = open(input_file)

    def __del__(self):
        """ Closes the input file """
        self.input_file.close()

    def has_more_tokens(self):
        """ Checks if there are more tokens to be analized """
        