"""
Module containing the vm writer class for the jack compiler.
"""

class VMWriter:

    def __init__(self, output):
        """ Creates a new file and prepares it for writing VM commands """
        self.output_file = open(output, 'w')

    def __del__(self):
        """ Closes the output file. """
        self.output_file.close()

    def write_push(self, segment, index):
        """ Writes a VM push command. """
        segment = segment.lower()

        if segment == "const":
            segment = "constant"
        elif segment == "arg":
            segment = "argument"

        self.output_file.write("push {} {}\n".format(segment, index))

    def write_pop(self, segment, index):
        """ Writes a VM pop command. """
        segment = segment.lower()

        if segment == "const":
            segment = "constant"
        elif segment == "arg":
            segment = "argument"

        self.output_file.write("pop {} {}\n".format(segment, index))

    def write_arithmetic(self, command):
        """ Writes a VM arithmetic command. """
        command = command.lower()

        self.output_file.write(command + '\n')

    def write_label(self, label):
        """ Writes a VM label command. """
        self.output_file.write("label {}\n".format(label))

    def write_goto(self, label):
        """ Writes a VM goto command. """
        self.output_file.write("goto {}\n".format(label))

    def write_if(self, label):
        """ Writes a VM if-goto command. """
        self.output_file.write("if-goto {}\n".format(label))

    def write_call(self, name, n_arg):
        """ Writes a VM call command. """
        self.output_file.write("call {} {}\n".format(name, n_arg))

    def write_function(self, name, n_locals):
        """ Writes a VM function command. """
        self.output_file.write("function {} {}\n".format(name, n_locals))

    def write_return(self):
        self.output_file.write("return\n")
