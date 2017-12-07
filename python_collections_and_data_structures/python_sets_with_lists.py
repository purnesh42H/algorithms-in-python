'''
Set operations can be performed with lists
'''               
def unioin(my_list, another_list):
    return list(set(my_list) | set(another_list))

def intersection(my_list, another_list):
    return list(set(my_list) & set(another_list))

def difference(my_list, another_list):
    return list(set(my_list) - set(another_list))     


def test_list_set_operations():
    my_list = [1, 2, 4, 17, 5, 6]
    another_list = [2, 6, 18, 19]
    assert len(unioin(my_list, another_list)) == 8
    assert len(intersection(my_list, another_list)) == 2
    assert len(difference(my_list, another_list)) == 4
    print('all {module} tests have {con}'.format(module='list with set operations', con='passed'))


test_list_set_operations()
