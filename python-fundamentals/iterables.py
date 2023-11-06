# iterables 

# map: apply the function on each of the iterables and return a map object that you can sum, turn to a list, etc.

jewels = "aA"
stones = "aAAbbbb"

# print(jewels.count(stones))

print(list(map(jewels.count, stones)))


jewels = "aA"
stones = "aAAbbbb"

# print(jewels.count(stones))

print(list(map(jewels.count, stones)))


# count how many chars in that string 
print('supercereal'.count('r'))


l1 = ["eat", "sleep", "repeat"]
print(list(enumerate(l1)))