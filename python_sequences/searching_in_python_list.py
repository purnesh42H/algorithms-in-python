'''
Any kind of searching is O(n)
'''
lst = [1, 2, 4, 6, 2, 3, 4, 5]
assert 2 in lst
assert lst.index(2) == 1
assert lst.count(4) == 2

# sorting
lst2 = sorted(lst)
lst.sort() # in place
assert lst == [1, 2, 2, 3, 4, 4, 5, 6]
assert lst2 == lst

# reverse
lst.reverse()
assert lst == [6, 5, 4, 4, 3, 2, 2, 1]

# unpacking
x, *y = [6, 5, 4, 4, 3, 2, 2, 1]
assert x == 6
assert y == [5, 4, 4, 3, 2, 2, 1]
