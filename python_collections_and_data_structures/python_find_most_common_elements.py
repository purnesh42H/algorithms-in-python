from collections import Counter

# find top N frequent elements
def find_most_common(lst, n):
     return Counter(lst).most_common(n)

def test_most_common():
    lst = [1, 2, 4, 5, 6, 6, 7, 7, 8, 888, 9, 9, 10, 6]
    assert find_most_common(lst, 2) == [(6, 3), (7, 2)]
    assert find_most_common(lst, 1) == [(6, 3)]

test_most_common()
    
