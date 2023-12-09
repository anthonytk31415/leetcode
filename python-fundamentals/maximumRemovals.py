
# Binary search the answer. That is a mother fucking doozey, but easy if you know what to do. 
# It takes linear time to check if p is a subset. And you do that logn times. 

# Time: O(n logn)
# Space: O(n) for the invalids 
def maximumRemovals(s, p , removable):
    left, right, = 0, len(removable) - 1

    while left <= right: 
        mid = (left + right)// 2
        invalidIndices = set(removable[:mid + 1])
        # is mid an answer? 
        pIdx = 0
        for i, sChar in enumerate(s):
            if pIdx >= len(p): break 
            if i not in invalidIndices and sChar == p[pIdx]:
                pIdx += 1

        # mid is a subset
        if pIdx >= len(p):  
            left = mid +1

        else: 
            right = mid - 1
    return left




# s = 'abacabaac'
# p = 'abac'

s = "abcacb"
p = "ab"
removable = [3,1,0]

# removable = [3,2,1]

s = "abcbddddd"
p = "abcd"
removable = [4,5,6]

print(maximumRemovals(s, p, removable))
