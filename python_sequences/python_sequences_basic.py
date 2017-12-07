'''
5 basic sequences are available in python
1) list - mutatble
2) tuple - immutable
3) bytearray - mutable
4) string - immutable
5) bytes - immutable
'''

some_list = []
assert str(type(some_list)) == "<class 'list'>"
some_string = ''
assert str(type(some_string)) == "<class 'str'>"
some_tuple = ()
assert str(type(some_tuple)) == "<class 'tuple'>"
some_ba = bytearray(b'')
assert str(type(some_ba)) == "<class 'bytearray'>"
some_bytes = bytes([])
assert str(type(some_bytes)) == "<class 'bytes'>"

'''
A named tuple is also available in the standard library, under the collections
package.
'''

'''
slicing operators
'''
some_string = 'Let us do it!'
assert some_string[:2] == 'Le'
assert some_string[2:] == 't us do it!'
assert some_string[:10:2] =='Ltu o'
assert some_string[:-2] == 'Let us do i'


'''
Copying mutable types
'''
#list
new_list = [1, 2, 3, 4]
some_list = new_list
new_list2 = list(new_list) # deep copy
new_list3 = new_list[:] # deep copy
assert new_list2 == new_list
assert new_list3 == new_list
assert new_list == some_list
new_list.pop()
'''
pop out the element even from some_list because saying list2 = list1
is actually saying point list2 where list1 is pointing
To preserve mutable types always do deep copy
'''

assert new_list2 == [1, 2, 3, 4]
assert new_list3 == [1, 2, 3, 4]
assert new_list == [1, 2, 3]
assert some_list == [1, 2, 3]

#set
new_set = {'a', 'b', 'c'}
some_set = new_set.copy()
some_set.discard('a')
some_set.remove('b')
assert str(some_set) == "{'c'}"

#dict
dict1 = { 1: 'hey', 2: 'Kay' }
dict2 = dict1.copy()
assert dict2 == dict1

# using copy module
import copy
another_list = copy.copy(new_list)
separate_list = copy.deepcopy(new_list)
assert separate_list == another_list
new_list.pop()
assert separate_list == another_list

test_str = 'all test have {con} in basics of {module}'
print(test_str.format(module='sequence', con = 'passed'))
