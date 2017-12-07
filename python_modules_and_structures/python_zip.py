'''
The zip function takes two or more sequences and creates a new sequence
of tuples where each tuple contains one element from each list
'''

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = ['a', 'b', 'c', 'd']

for item in zip(lst1, lst2):
    print(item)

# Note that the items are matched in their sequence. If one sequence has more
# elements the residual elements in that will be igonored.



