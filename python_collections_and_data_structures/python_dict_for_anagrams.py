from collections import Counter

# using built-in dict
def get_char_counts(word):
    counter = {}
    for char in word:
        counter.setdefault(char, 0)
        counter[char] += 1

    return  counter

def has_same_chars(counter1, counter2):
    for key, value in counter1.items():
        if key not in counter2:
            return False
        elif value != counter2[key]:
            return False

    return True
    
def is_anagram(word1, word2):
    word1_char_counts = get_char_counts(word1)
    word2_char_counts = get_char_counts(word2)
    return has_same_chars(word1_char_counts, word2_char_counts)

# using Counter
def is_anagram_using_counter(word1, word2):
    return Counter(word1) == Counter(word2)

def test_is_anagram():
    word1 = 'abcdef'
    word2 = 'cdefab'
    assert is_anagram(word1, word2) == True
    assert is_anagram('bcdef','acdef') == False

    assert is_anagram_using_counter(word1, word2) == True
    assert is_anagram_using_counter('bcdef','acdef') == False

test_is_anagram()
    
    
