# colon sample
# isisomorphic


def play(s, t):
    d = {}              # dictionary mapping of unique letters in s to unique letters in t
    value_set = set()   # keeps track of when a letter in t is mapped to a letter; if it occurs more than once, return False
    
    for index, letter in enumerate(s):
        print(index, letter)
        print(f'd = {d}')
        print(f'value_set = {value_set}')
        try:        # two failures; (1) and (2) 
            # (1) fail: a letter in s after conversion does not equal that letter in t at the same index
            if d[letter] != t[index]:
                print('1 executing')
                return False
        except KeyError:             
            print('2 executing')
            d[letter] = t[index]
            # (2) fail: a letter in s has already been defined but doesn't match with the letter 
            # i.e. a repeat of the same char in s is a different repeat
            if d[letter] in value_set:
                print('3 executing')
                return False
            value_set.add(d[letter])


    return True    

print(play('abc', 'abb'))