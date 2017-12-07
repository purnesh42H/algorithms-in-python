from collections import defaultdict
import string

def removePunctuations(word):
    strip = string.whitespace + string.punctuation + string.digits + "\"’"
    return word.strip(strip).strip()

def count_unique_words(seq):
    word_counter = defaultdict(int)
    for word in seq.split():
        hashable_word = removePunctuations(word)
        if len(hashable_word) > 2:
            word_counter[hashable_word] += 1 

    for word in word_counter:
        print ('{word} appears {count} times'.format(word=word, count=word_counter[word]))

seq = 'blah blah, blah, kale, something, i like it a lot, 122'
count_unique_words(seq)
