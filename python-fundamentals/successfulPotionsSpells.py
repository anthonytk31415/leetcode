from bisect import bisect_left

# brute force: O(M*N)

# def successfulPairs(spells, potions, success):
#     pairs = []
#     potions.sort()
#     for i in range(len(spells)):
#         potions_left = len(potions)
#         for j in range(len(potions)):
#             if spells[i]*potions[j] >= success: 
#                 break
#             else: 
#                 potions_left -= 1
#         pairs.append(potions_left)
#     return pairs

def binarySearch(success, potions, p, r):
    if p > r: 
        print('0 triggers')
        return r
    if p == r: 
        if potions[p] >= success:
            print('1 triggers')
            return p 
        elif potions[p] < success:
            print('thisi triggers')
            return p+1
    q = (p + r)//2
    if potions[q] >= success:
        return binarySearch(success, potions, p, q)
    elif potions[q] < success:
        return binarySearch(success, potions, q+1, r)


spell = 1
success = -5/spell
potions = [0,1,2,3,4,5,6,7,8] ## 4


# print(binarySearch(success, potions, 0, 8))

def successfulPairs2(spells, potions, success):
    pairs = []
    potions.sort()
    for i in range(len(spells)):
        pairs.append(len(potions) - binarySearch(success/spells[i], potions, 0, len(potions)-1))
    return pairs






# from bisect import bisect_left

# def successfulPairs(spells, potions, success):
#     pairs = []
#     potions.sort()
#     for i in range(len(spells)):
#         idx = bisect_left(potions, success/spells[i])
         
#         pairs.append(max(0, len(potions) - idx))
#     return pairs




# spells = [5,1,3]
# potions = [1,2,3,4,5]
# success = 7

# spells = [3,1,2]
# potions = [8,5,8] 
# success = 16

spells = [9,39]
potions = [35,40,22,37,29,22]  ## [22,22,29,35, 37, 40]
success = 320
#>> need [2,6]
print(successfulPairs2(spells, potions, success))