def dict_set_operations():
    d1 = {1: 'a', 2: 'b', 3: 'c'}
    d2 = {1: 'a', 4:'d'}
    assert list(d1.keys() & d2.keys()) == [1]
    assert list(d1.items() & d2.items()) == [(1, 'a')]
    assert list(d1.keys() - d2.keys()) == [2, 3]
    assert len(d1.items() - d2.items()) == 2 # why shouldn't we equate the list items?
    print(list(d1.items() - d2.items()))

dict_set_operations()
