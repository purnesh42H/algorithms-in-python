'''
Immutable type with values separated by commas
'''

t1 = 3405, 'some string'
assert t1[0] == 3405
assert t1 == (3405, 'some string')
t2 = t1, (1, 2, 3, 4, 5)
assert t2 == ((3405, 'some string'), (1, 2, 3, 4, 5))

'''
Creating single value tuple
'''
t3 = () # empty
assert len(t3) == 0
t4 = ('some string',) # single value tuple
# Note it is not possible to enclose one value within brackets
assert len(t4) == 1

'''
Tuple methods
'''
t5 = (1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7)
assert t5.count(7) == 3
assert t5.index(4) == 3

'''
Tuple unpacking
'''
x, *y = [1, 2, 3, 4]
assert x == 1
assert y == [2, 3, 4]
'''
In Python, any iterable can be unpacked using the sequence unpacking operator,
*. When used with two or more variables on the left-hand side of an
assignment, one of which preceded by *, items are assigned to the variables,
with all those left over assigned to the starred variable
'''

'''
Named Tuples
Same as built in tuple but you can refer the items by name as well as index
'''
from collections import namedtuple

named_tuple = namedtuple('name', ['name1', 'name2'])
t6 = named_tuple('Jackie', 'Chris')
assert t6.name1 == 'Jackie'
assert t6.name2 == 'Chris'

s = 'all {module} test cases {con}'
print(s.format(module = 'tuple', con = 'passed'))
