#!/usr/bin/env python
""" Module-level docstring

Module-level docstrings are used to capture whatever the coder feels is necessary
to know when using the entirety of the script. It should contain any descriptions
of global variable, a description of the usage (when used from the command line),
and any arguments that the program accepts/expects.

In addition to this, I believe this is a great place to put 'pseudocode' when 
starting out your project.

Usage: python my_program.py [OPTIONS]

Args:
    first_arg (type of arg): description of argument

"""
#-- START IMPORTS --#

import sys

#-- STOP IMPORTS --#

# Define your first function
def main(arg_name, kwarg_name = None):
    """ Function-level docstring
    
    The purpose of a function docstring is to indicate to the user the purpose
    and usage of a given function. Additionally, it should describe what the
    function expects as arguments (or 'signature'), and what it will give back 
    (or 'return')to the user after it is done.
    
    Args:
        arg_name (str): some string type argument, like a filename
        kwarg_name (int): possibly an integer, but if nothing is given, uses None
    
    Returns:
        Some output to be defined below
    """
    pass


# This next part confuses a lot of people. It is okay if you don't understand
# this right away. The purpose of 'if __name__ ...' is to check to see if the
# script is being called from the terminal (or command line).

# When a program is used from the command line, it gets a special tag called 
# '__main__' attached to it. If this tag is present, it can follow a specialized
# (or curated) workflow specific to working at the command line.
#
# With this section below, a script is made to be both 'importable' and 'invokable'.
if __name__ == '__main__':
    expected_first_arg = sys.argv[1]
    expected_second_arg = sys.argv[2]
    main(expected_first_arg, expected_second_arg)