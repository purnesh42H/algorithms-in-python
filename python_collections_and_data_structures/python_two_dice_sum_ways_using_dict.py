from collections import defaultdict

def get_number_of_ways():
    num_ways = defaultdict(int)
    for i in range(1, 6+1):
        for j in range(1, 6+1):
            num_ways[i+j] += 1

    return num_ways

def get_sum_probability(s):
    if s > 12 or s < 2:
        return None
    return (get_number_of_ways()[s] / 36).as_integer_ratio()
    
def test_number_of_ways():
    print(get_number_of_ways())
    print(get_sum_probability(6))

test_number_of_ways()
