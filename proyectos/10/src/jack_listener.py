"""
Module containing a Listener implementation for the Jack analizer.
It uses the listener generated by the ANTLR4 tool.
"""

from JackGrammarListener import JackGrammarListener
from JackGrammarParser import JackGrammarParser

class Listener(JackGrammarListener):
    """
    Class that defines the behaviour of a Grammar Listener for the Jack Compiler.

    It inherits from the default listener generated by the ANTLR4 parser/lexer generator tool,
    so it is necessary to make sure that the default listener has been generated before trying to use this class.
    """

    KEYWORDS = ["class", "constructor", "function", "method", "field", "static", "var", "int", "char", "boolean", "void", "true", "false", "null", "this", "let", "do", "if", "else", "while", "return"]
    SYMBOLS = ['{', '}', '[', ']', '(', ')', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
    NON_TERMINAL_XML = ["class", "classVarDec", "subroutineDec", "parameterList", "subroutineBody", "varDec", "statements", "whileStatement", "ifStatement", "returnStatement", "letStatement", "doStatement", "expression", "term", "expressionList"]

    def __init__(self, parser, output_file):
        """ Constructor. Opens the output file with write permissions. """

        self.parser = parser
        self.output_file = open(output_file, 'w')
        self.indent_string = "  "
        self.indent_level = 0

    def __del__(self):
        self.output_file.close()

    def enterEveryRule(self, ctx):
        """ Opens an xml tag corresponding to the current Non-terminal and writes it to the output file """

        tag = self.parser.ruleNames[ctx.getRuleIndex()][:-2]
        if tag in Listener.NON_TERMINAL_XML:
            open_tag = "{}<{}>\n".format(self.get_current_indent(), tag)
            self.output_file.write(open_tag)
            self.increase_indent()
        return super().enterEveryRule(ctx)

    def exitEveryRule(self, ctx):
        """ Closes an xml tag corresponding to the current Non-terminal and writes it to the output file """

        tag = self.parser.ruleNames[ctx.getRuleIndex()][:-2]
        if tag in Listener.NON_TERMINAL_XML:
            self.decrease_indent()
            close_tag = "{}</{}>\n".format(self.get_current_indent(), tag)
            self.output_file.write(close_tag)
        return super().exitEveryRule(ctx)

    def visitTerminal(self, node):
        """ Writes the corresponding terminal tag to the xml output file """

        terminal_value = node.getText()
        tag = self.get_terminal_group(terminal_value)
        # remove quotation marks from a string
        if tag == "stringConstant":
            terminal_value = terminal_value[1:-1]
        # check if an integer is valid according to the architecture
        elif tag == "integerConstant":
            int_value = int(terminal_value)
            # if the value is not valid, throw an error
            if int_value < 0 or int_value > 32767:
                print("Value Error: Integer value [{}] not supported by the int data type".format(int_value))
                exit(-1)
        # change the < > symbols for valid ones (xml)
        elif tag == "symbol":
            if terminal_value == '<':
                terminal_value = "&lt;"
            elif terminal_value == '>':
                terminal_value = "&gt;"
            elif terminal_value == '&':
                terminal_value = "&amp;"
            elif terminal_value == '"':
                terminal_value = "&quot;"
        # write to the output file
        self.output_file.write("{0}<{1}> {2} </{1}>\n".format(self.get_current_indent(), tag, terminal_value))
        return super().visitTerminal(node)

    
    def get_current_indent(self):
        return self.indent_level * self.indent_string

    def increase_indent(self):
        self.indent_level += 1

    def decrease_indent(self):
        self.indent_level -= 1

    def get_terminal_group(self, terminal):
        
        if terminal in Listener.KEYWORDS:
            group = "keyword"
        elif terminal in Listener.SYMBOLS:
            group = "symbol"
        elif '"' in terminal:
            group = "stringConstant"
        elif terminal.isdigit():
            group = "integerConstant"
        elif terminal.isalnum():
            group = "identifier"

        return group