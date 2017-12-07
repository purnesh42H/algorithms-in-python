# Two methods to find the occurence of a string in another string
# index(s), find(s)
# both returns the index of string s if present
# index raises a value error if not found
# find returns -1 if not found


s = 'Some string long long'
assert s.find('o') == 1
assert s.index('o') == 1
assert s.find('z') == -1

# counting the occurences
assert s.count('o') == 3
assert s.count('o', 0, -5) == 2

# replacing in string
s = 'Chris is Chris Who is Chris'
assert s.replace('Chris', 'Who') == 'Who is Who Who is Who'
assert s.replace('Chris', 'Who', 2) == 'Who is Who Who is Chris'
