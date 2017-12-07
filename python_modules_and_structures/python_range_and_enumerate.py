'''
enumerate will return the index and item of the sequence
'''

some_list = [1, 2, 4, 5, 6]

for index, value in enumerate(some_list):
    print(index, value)

some_dict = {1: 'hi', 2: 'how', 3: 'are', 4: 'you?'}

for index, key in enumerate(some_dict):
    print(index, key, some_dict[key])
    

'''
range will run the look from [x, y)
'''

for x in range(0, len(some_list)):
    print(x, some_list[x])
    
