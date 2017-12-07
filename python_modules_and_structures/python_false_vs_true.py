# False and True in python
'''
False is defined by the predefined constant False, or the special object None,
or by an empty sequence of collection (empty string ’’, list [], or tuple
()). Anything else is True. It is also possible to assign the result of a
comparison or other Boolean expression to a variable
'''
not_null = '' or 'string1' or 'string2'
assert not_null == 'string1'

'''
Google style guide sets the following rules for using implicit False in Python.
1. Never use == or != to compare singletons, such as the built-in variable
None. Use is or is not instead.
'''
assert ([1] is not None) == True

'''
Beware of writing if x: when you really mean if x is not None.
1. Never compare a boolean variable to False using ==. Use if not x:
instead. If you need to distinguish False from None then chain the
expressions, such as if not x and x is not None:

2. For sequences (strings, lists, tuples), use the fact that empty sequences
are False, so if not seq: or if seq: is preferable to if len(seq):
or if not len(seq):

3. When handling integers, implicit False may involve more risk than
benefit, such as accidentally handling None as 0:
'''
some_object = ()
a = 5
# Good
if not some_object:
    print('No object')

if a == 0:
    print('a is zero')

if a % 10 != 0:
    print('a is not multiple of 10')


# Bad
if len(some_object) == 0:
    print('No object')

if not a:
    print('a is zero')

if not a % 10:
    print('a is not multiple of 10')
