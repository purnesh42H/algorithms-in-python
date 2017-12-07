# Cast string number to any base
# Eg: 15
assert int('1111', 2) == 15
assert int('17', 8) == 15
assert int('15', 10) == 15

# No. of bits to represent an integer in python
assert (100).bit_length() == 7

# Different representations
print(bin(888))
print(hex(888))
print(oct(888))


# comparing floats
def compare(x, y, places=7):
    return round(x, places) == round(y, places)

print(compare(111/7, 15.857, 3)) # correct way of comparison
print(111/7 == 15.8571429) # Incorrect way of comparing floats


# Methods for numbers
print(divmod(45, 6)) # returns quotient and remainder

'''
The method round(x, n) returns x rounded to n integral digits if n is a
negative int or returns x rounded to n decimal places if n is a positive int.
The returned value has the same type as x:
'''
assert round(98.9689, 2) == 98.97
assert round(98.96,-2) == 100


# Get fractional representation of float
print((2.75).as_integer_ratio())

# Use decimal.Decimal module if you do not want deal with rounding and subtraction
from decimal import Decimal
assert sum (Decimal ("0.1") for i in range(10)) == Decimal("1.0") # Correct

# Nice way of string formatting
s = 'Tests in {name} have {con}!'
print(s.format(name='this module', con='passed'))

assert sum (0.1 for i in range(10)) == 1.0 #Wrong
