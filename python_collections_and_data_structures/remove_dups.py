import string
from collections import OrderedDict

# removes dups from string composed of ascii chracters
def remove_dups(word):
    word_dict = OrderedDict() # Why use OrderedDict??? Why not a set??
    for char in word:
        word_dict.setdefault(char, 1)

    return ''.join(list(word_dict.keys()))

def test_remove_dups():
    word = 'google'
    assert remove_dups(word) == 'gole'

test_remove_dups()
    
        
