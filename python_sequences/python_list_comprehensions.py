'''
A list comprehension is an expression and loop (with an optional condition)
enclosed in brackets
'''
lst = [y for y in range(1, 10)]
assert lst ==  [1,2,3,4,5,6,7,8,9]
a = [y for y in range(1900, 1940) if y%4 == 0]
assert a == [1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936]

pow_a = [2**y for y in range(1, 10)]
assert pow_a ==  [2,4,8,16,32,64,128,256,512]


'''
The Google Python Style guide endorses list comprehensions and generator expressions
saying that “they provide a concise and efficient way to create lists and iterators
without resorting to the use of map(), filter(), or lambda.”
'''

'''
The Google Python Style Guide advocates that list comprehensions
should only be used for simple cases, when each portion fits in one line
(no multiple for clauses or filter expressions):
'''

# Good
result = []
for x in range(10):
    for y in range(5):
        if x * y > 10:
            result.append((x, y))

# Bad
result = [(x, y) for x in range(10) for y in range(5) if x * y >
10]

'''
Nice example:
return ((x, complicated_transform(x))
    for x in long_generator_function(parameter)
        if x is not None)
'''

def some_long_list_comprehension_methon():
    for x in range(5):
        for y in range(5):
            if x != y:
                for z in range(5):
                    if y != z:
                        yield (x, y, z)

print(some_long_list_comprehension_methon())
