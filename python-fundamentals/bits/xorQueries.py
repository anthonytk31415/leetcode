from functools import lru_cache

# this implementation is an N^2 memoization operation

def xorQueries1(arr, queries):
    @lru_cache(None)
    def query(idx1, idx2):
        curRes = arr[left]
        if left != right: 
            for i in range(left + 1, right + 1):
                curRes ^= arr[i]
        return curRes
    res = []
    for left, right in queries: 
        res.append(query(left, right))
    return res

# This is O(N); it uses the concept of prefix sum

def xorQueries(arr, queries):
    for i in range(len(arr) - 1):
        arr[i + 1] ^= arr[i]
    return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]



# print(bin(1 ^ 3))
# print(1 ^ 3)

# print(8^8)


arr = [1,3,4,8]

arr1 = [1, 3^1, 4^3^1, 8^4^3^1]
# (i, j)
# aj ^ ai-1

# An important property of XOR bits: 
# x ^ y ^ x = y
# x ^ x = 0
# (x ^ y) ^ z = x ^ (y ^ z)  

# with the prefix sum, you since you have a the prefix of all the XORs from 0 - n, 
#prefix(x) XOR prefix(y-1) gives you XOR from y to x 

arr = [1,15,22,47]
prefix = [x for x in arr]
for i in range(len(arr) - 1):
    prefix[i+1] ^= prefix[i] 

# these should be the same
print(15^22^47)
start, end = (1, 3)
print(prefix[end]- prefix[start - 1])

# print(3^1^1)


queries = [[0,1],[1,2],[0,3],[3,3]]

print(xorQueries(arr, queries))

# print(1^3)
# print(3^4)
# print(1^3^4^8)
# print((1^3)^(4^8))