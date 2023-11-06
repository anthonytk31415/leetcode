def majority_char(s):
    d = {}
    for char in s: 
        if char not in d.keys():
            d[char] = 1
        else:
            d[char] +=1
    max_value = max(d.values())
    print(max_value)
    max_keys = [pair for pair in d.items() if pair[1]==max_value]
    if len(max_keys) > 1:
        return False
    elif len(max_keys) == 1 and max_keys[0][1] > len(s)/2:
        return True
    else: 
        return False 

# str = 'all'
# str2 = 'welcome to the jungle'

# print(majority_char(str))           # 'l'
# print(majority_char(str2))          # None


jewels = "aA"
stones = "aAAbbbb"

# print(jewels.count(stones))

print(list(map(jewels.count, stones)))


# count how many chars in that string 
print('supercereal'.count('r'))

# map: apply the function on each of the iterables and return a map object that you can sum, turn to a list, etc.
