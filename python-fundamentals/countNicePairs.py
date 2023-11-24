from collections import defaultdict


# This answer is kind of like twoSum, with an Time: O(n) solution. Space: O(n) for the delta storage and the list as well. 

# We notice that with algebra, for any x, y with valid index, x - rev(x) = y - rev(y)
# So for those with common deltas, we append them to a list and we increase our res by the sum of the (length - 1)
# which are the valid pairs. 


def countNicePairs(nums):
    deltas = defaultdict(list)

    for i, x in enumerate(nums): 
        rev_x = int(str(x)[::-1])
        delta = x - rev_x
        deltas[delta].append(i)

    res = 0
    for delta in deltas: 
        n = len(deltas[delta]) - 1
        res += n * (n + 1) / 2

    return int(res) % (10 ** 9 + 7)

# x = 120
# print(int(str(x)[::-1]))
nums = [13,10,35,24,76]
print(countNicePairs(nums))

# print(int("021"))