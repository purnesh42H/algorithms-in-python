# unicode strings
# Starting from Python 3, all strings are
# now Unicode, not just plain bytes.
# Unicode character with the ordinal value 0x0020.
s = u'some\u0020string'
assert s == 'some string'

# Best way to join python strings
lst = ['1', '2', '3']
assert ''.join(lst) == '123'
assert ', '.join(lst) == '1, 2, 3'

# Adding chars to start/end of python string
name = 'John Adams'
assert name.rjust(50, '-') == '----------------------------------------John Adams'
assert name.ljust(50, '-') == 'John Adams----------------------------------------'

# string mapping
# ** is unpacking operator and it produces key-value list suitable to passing
# to a function
# locals() get's the local variables in scope
string = 'hello'
number = 999
assert '{string} {number}'.format(**locals()) == 'hello 999'

# python string split
s = 'hello\nAnna'
assert s.splitlines() == ['hello', 'Anna']
s2 = 'kale*salad-base*hate'
assert s2.split('*') == ['kale', 'salad-base', 'hate']


#string strip
s3 = 'kale888'
assert s3.strip('888') == 'kale'
# lstrip and rstrip can strip characters from beginning and end repectively

# changing case of python strings
str_demo = 'cHRIS'
assert str_demo.swapcase() == 'Chris'
assert 'chris'.capitalize() == 'Chris'
assert 'chris'.upper() == 'CHRIS'
assert 'CHRIS'.lower() == 'chris'

# string formatting
s = 'All tests in {module} has {con}'
print(s.format(module = 'string', con = 'passed'))

s = 'All tests in {0} has {1}'
print(s.format('string', 'passed'))

s = 'All tests in {} has {}'
print(s.format('string', 'passed'))

# s to force string form, r to force representational
# form, and a to force representational form but only using ASCII characters
import decimal
print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9")))



