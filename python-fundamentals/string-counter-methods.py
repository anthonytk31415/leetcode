


a = 'the cat in the hat came back and look at him' 


from collections import Counter

## splits at the delimiter in the quotes
a_word_array = a.split(' ')

## joins array of strings with the char of choice
a_joined = ' '.join(a_word_array)

## for each element in the list, count it from a dictionary
a_word_count = Counter(a_word_array)

a_char_count = Counter(a)