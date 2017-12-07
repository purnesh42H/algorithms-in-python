"""
Big-O Efficiency of Python Dictionary Operations
Operation Big-O Efficiency
copy O(n)
get item O(1)
set item O(1)
delete item O(1)
contains (in) O(1)
iteration O(n)
"""

# Iterating over dictionaries

def set_default_dict():
    d = {}
    for i, num in enumerate([3,4,5,6,8,9,6,5]):
        d.setdefault(num, []).append(i)

    return d

d = set_default_dict()

print('iterating over keys')
for key in sorted(d):
    print ('{key} = {value}'.format(key=key, value=d[key]))

print('iterating over key, value')
for key, value in d.items():
    print ('{key} = {value}'.format(key=key, value=value))
           
