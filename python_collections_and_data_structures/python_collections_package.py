# defaultdict
'''
Default Dict. Can be used if your dictionary values are of same types.
It handles the cases of key being not present very gracefully
'''

from collections import defaultdict

'''
using built-in dict
'''
d1 = {}
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for key, value in pairs:
    if key not in d1:
        d1[key] = []
    d1[key].append(value)

'''
using defaultdict
'''
d2 = defaultdict(list)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

for key, value in pairs:
    d2[key].append(value)

s = '{name} = {dict}'
print(s.format(name='d1', dict=d1))
print(s.format(name='d2', dict=d2))

# OrderedDict
from collections import OrderedDict
'''
maintains the order in which the keys are inserted
'''
d = OrderedDict()
d[1] = 'a'
d[3] = 'c'
d[2] = 'b'

print(d)
print('sorted dict')
print(OrderedDict(sorted(d1.items(), key=lambda x: x[0])))

# Counter
from collections import Counter

print('Counter example')
def counter_example():
    'count occurrences'
    seq1 = [1, 2, 3, 5, 1, 2, 5, 5, 2, 5, 1, 4]
    print('sequence={}'.format(seq1)) 
    seq_counts = Counter(seq1)
    print(seq_counts)
    '''we can increment manually or use the update() method'''
    seq2 = [1, 2, 3]
    seq_counts.update(seq2)
    print(seq_counts)
    seq3 = [1, 4, 3]
    for key in seq3:
        seq_counts[key] += 1
    print(seq_counts)
    '''also, we can use set operations such as a-b or a+b '''
    seq_counts_2 = Counter(seq3)
    print(seq_counts_2)
    print(seq_counts + seq_counts_2)
    print(seq_counts - seq_counts_2)

counter_example()
