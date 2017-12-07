'''
Set is unordered collection
Insertion - O(1)
Union - O(m + n)
Intersection - O(n)
'''

'''
Frozen sets are immutable objects that only support methods and operators
that produce a result without affecting the frozen set or sets to which
they are applied.
'''

# Adding element to set
unique_names1 = {"mike", "charles", "brian"}
unique_names1.add("hasting") # it will make sure that element is added only once
assert "hasting" in unique_names1
# Note you should not compare sets by == as the order will not be maintained

# update sets
unique_names2 = set() #another way of instantiating an empty set
unique_names2.add("boss")
unique_names1.update(unique_names2) # updates the set unique_names1 with unique_names2
assert "boss" in unique_names1
unique_names2.add("chris")
unique_names1|=unique_names2 # another way of updating sets
assert "chris" in unique_names1

# union of two sets
unique_names3 = {"maria", "anna", "geroma"}
unique_names5  = unique_names1.union(unique_names3) # or unique_names1 | unique_names3 # returns a new set
assert len(unique_names5) == 9

# intersection of two sets
unique_names4 = {"mike", "charles", "jack"}
unique_names6 = unique_names5.intersection(unique_names4) # returs a new set. What should be finally in unique_names1?? Can you tell?
assert len(unique_names6) == 2

# subtracting two sets
unique_names7 = {"maria"}
unique_names5  = unique_names5.difference(unique_names7) # returns a new set
assert len(unique_names5) == 8

# clear sets
unique_names5.clear()
assert len(unique_names5) == 0

'''
The discard(x), remove(x), and pop() Methods:
discard(x) removes the item x from the set. remove(x) removes the item
x from the set or raises a KeyError exception if the element is not in the set.
pop() returns and removes a random item from the set or raises a KeyError
exception if the set is empty.
''


