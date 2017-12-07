'''
Note that functions are also treated as objects in python. When def is
executed, a function object is created together with its object reference.

If we do not define a return value, Python automatically returns None

An activation record happens every time we invoke a method: information
is put in the stack to support invocation.
'''

# Default values in module
'''
Whenever you create a module, remember that mutable objects should not
be used as default values in the function or method definition:
'''

#Good
def func(a, b=None):
    if b == None:
        b = []
    b.append(a)
#Bad
def func(a, b=[]):
    b.append(a)

# The __init__.py file
'''
A package is a directory that contains a set of modules and a file called
__init__.py . This is required to make Python treat the directories as
containing packages, preventing directories with a common name (such as
“string”) from hiding valid modules that occur later on the module search
path:
'''


# The __name__ variable
'''
Whenever a module is imported, python creates a variable for it called __name__
and store's the module's name in this variable
'''
# Byte-coded Compiled Modules
'''
When the Python interpreter is invoked with the -O flag, optimized
code is generated and stored in .pyo files. The optimizer removes assert
statements. This also can be used to distribute a library of Python code
in a form that is moderately hard to reverse engineer
'''

# sys module
'''
The variable sys.path is a list of strings that determines the interpreter’s
search path for modules. It is initialized to a default path taken from the environment
variable PYTHONPATH, or from a built-in default. You can modify
it using standard list operations:
'''
import sys
import os
sys.path.append(os.path.abspath('../')) # add the parent folder path

'''
The variable sys.argv allows us to use the arguments passed in the
command line inside our programs
'''
import sys

def main():
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == 'main':
    main()

# The dir() method
'''
We can get list of methods and variables of a obeject.
It returns the sorted list all types of names: variables, modules, functions.
'''
import sys
print(dir(sys))
