# filter
'''
It filters the elements from a given sequence based on specified criteria
'''

def divisible_by_3(num):
    return num % 3 == 0

def test_filter():
    print('Filteres numbers divisible by 3')
    div_by_3 = filter(divisible_by_3, range(2, 25))
    assert next(div_by_3) == 3
    assert next(div_by_3) == 6
    
    for item in filter(divisible_by_3, range(2, 25)):
        print(item)

test_filter()

# map
'''
applies a particular function to each element in list.
'''
def power(x):
    return x*x

def test_map():
    print('squares each element')
    for i, item in enumerate(map(power, range(2, 10))):
        print(i+2, item)

test_map()


# lambda
'''
The lambda function is a dynamic way of compacting functions inside the
code. 
'''
def area_rect(l, b):
    return l * b

# above function can be re-written as

rect_area = lambda l, b: l*b

def test_area():
    l = 15
    b = 10
    assert area_rect(l, b) == 150
    assert rect_area(l, b) == 150
    print('{hof} tests are passed'.format(hof='lambda'))


test_area()

# lambda are very useful in creating keys for dictionary
from collections import defaultdict
message_dict = defaultdict(lambda: "No message")

