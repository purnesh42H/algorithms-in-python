'''
Dictionaries in python is implemented using hash table
hash(item) computes a unique integer value of an item
'''

print(hash(42))
print(hash('Cashew'))


'''
A dict is a collection mapping type that is iterable and supports the
membership operator in and the size function len(). Mappings are collections
of key-value items, providing methods for accessing items and their
keys and values. When iterated, unordered mapping types provide their
items in an arbitrary order.

Accessing dictionaries has runtime O(1) so they are used to keep counts
of unique items (for example, counting the number of each unique word in a
file) and for fast membership test. Dictionaries are mutable, so we can easily
add or remove items, but since they are unordered, they have no notion of
index position (so that they cannot be sliced or striped):
'''

# adding elements to dictionary
d = {}
d['a'] = 1
assert d['a'] == 1
d['b'] = dict()
d['b']['a'] = 2
print(d)

d.setdefault('b', 2) # It returns the value of key if it already exists and adds the key with default value, otherwise
# look at this example:

def normal_dict():
    d = {}
    for i, num in enumerate([3,4,5,6,8,9,6,5]):
        if num not in d:
            d[num] = []
        d[num].append(i)

    return d

def set_default_dict():
    d = {}
    for i, num in enumerate([3,4,5,6,8,9,6,5]):
        d.setdefault(num, []).append(i)

    return d

print(normal_dict())
print(set_default_dict())

# important methods for dictionary
d1 = dict()
d1.update(d) # update d1 with key-value pairs of d
print(d1)

employee = dict(name='xyz', dept='IT') # A more readable way of creating dict object
assert employee.get('name') == 'xyz' # get value of a key

# dictionary views
'''
A dictionary view is effectively a read-only iterable object that appears to
hold the dictionary’s items or keys or values:
'''
print(employee.keys())
print(employee.items())
print(employee.values())

# Removing from dictionary
d1.pop('a') # removes the value of key given
d1['a'] = 1
d1.popitem() # removes an arbitrary element from the dictionary
print(d1)

d1.clear()
assert len(d1) == 0

'''
According to google style guide
[Good] for key in adict: ...
            if key not in adict: ...
[Bad] for key in adict.keys(): ...
            if not adict.has_key(key): ...
'''

# One of very cool thing dict can achieve for you is reducing your branching conditions:

def add(a, b):
    return a + b

def assign(a, b):
    a = b
    return a
    
def normal_branching(action, a, b):
    if action == 'add':
        return add(a, b)
    if action == 'assign':
        return assign(a, b)

actions = dict(add=add, assign=assign)
def reduced_branching_using_dict(action, a, b):
    return actions[action](a, b)

def test_branching():
    assert normal_branching('add', 5, 4) == reduced_branching_using_dict('add', 5, 4)
    a1, a2 = 0, 0
    a1 = normal_branching('assign', a1, 4)
    a2 = reduced_branching_using_dict('assign', a2, 4)
    assert a1 == a2
    print('All test for dictionary are passed')

test_branching()

    




