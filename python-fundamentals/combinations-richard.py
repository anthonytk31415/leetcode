# combinations-richard.py
# array of integers 
# https://leetcode.com/problems/combinations/solutions/?orderBy=most_votes
# https://leetcode.com/problems/combinations/solutions/27024/1-liner-3-liner-4-liner/?orderBy=most_votes


# n!/(k! * (n-k)!)

## test cases for combinations
# [1,2,3]
# [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
# n = 0
# [[]] --> length 1

# n = 1
# [1] 
# [[], [1]] --> length 2
# [1,2]
# n = 2
# [[], [1]] 2 + [[], [1]] 
# (1), 2+ (1) -> (1,2)
# [[], [1], [2], [1, 2]] --> length 4
# n = 3
# (1,2) + 3 + (1,2)
# [[], [1], [2], [1, 2]] = 3 + [[], [1], [2], [1, 2]]
# [3], [3, 1], [3, 2], [3, 1, 2] --> length 8

# time complexity: O(n^2)
# space complexity: O(2^n)

# feedback: 
# backtracking 
# a bit chaotic
# get more hints 
# - review time and space complexity immediately 

############################################################################################################
## combinations: from k  0 to n (n length of array of items to permute)
## (order does not matter)
##
## Returns all combinations from k = 1 to k = len(arr)
## Concept: start with empty, then build up to K elements
## with each iteration, combine the old answer + new element added + (old answer) 
## and do this k times i.e. length of array
############################################################################################################
def combination(arr):
    cur = [[]]
    for x in arr:
        cur = cur + [y + [x] for y in cur]        

    #now return no dupes - use a set!
    return [list(y) for y in set([tuple(x) for x in cur])]

    # below is another way of writing the 'no dupes'     
    # res = []
    # for x in cur:
    #     if x not in res: 
    #         res.append(x)


# review this line [x for x in set(cur)]
# this did not work because lists are mutable; in sets, your elements cannot be mutable
# you can turn each list into a tuple, then put them in a set, then turn the set back into a list

# test case for no dupes
# arr = [1,2,2]
# print(combination(arr))

# array of n elements, choose k elements


############################################################################################################
# combination: n choose k
# - order does not matter
############################################################################################################
## main idea:
## base case of k = 1: return the array of k elements (choose only 1)
## for items larger than k: 
## (n choose k) = elem1 + (n-1 choose k - 1), ..., elem n-1 + ((n-(n-1) choose k-1), elem(n + (0 choose k)))
## note that when n < k there is no combination 
############################################################################################################
def combinationK(arr, k):
    if k == 1: 
        return arr                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    res = []
    for i in range(len(arr)):
        x = arr[i] 
        new_arr = arr[i+1:]
        if len(new_arr) >= k-1:
            for y in combinationK(new_arr, k-1):
                res.append(x + y)
    return res
        

# print(combinationK(['a','b','c','d'], 3))

# 4 choose 3
# = for each element in array: 
# e1 + (3 choose 2 e2,e3,e4) + e2(2 choose 2 e3, e4) + e3(1 choose 2 e4) + e4(0 choose 2 Nil)
# abc abd acd; bcd; 


# 1 choose 1:
# --> a(0 choose 0)

# #examples:
# 1 choose 2: 
# a --> None
# 2 choose 2: 
# a,b --> a,b
# --> a(1 choose 1) + b(0 choose 1)

# 3 choose 2: 
# a,b,c 
# --> ab, ac, bc 
# --> a+(2 choose 1 of b, c) + b (1 choose 1 c) + c (0 choose 1)

# abcd
# 4 choose 2
# a(3 choose 1 of b,c,d) + b(2 choose 1 c,d) + c(1 choose 1 d) + d(0 choose 1)

# ab, ac, ad; bc, bd; cd; 

# ##############
# 4 choose 3 (abcd)
# --> a(3 choose 2 bcd) + b(2 choose 2 cd) c(1 choose 2 d) + d(0 choose 2)

# = for each element in array: 
# e1 + (3 choose 2 e2,e3,e4) + e2(2 choose 2 e3, e4) + e3(1 choose 2 e4) + e4(0 choose 2 Nil)
# abc abd acd; bcd; 



############################################################################################################
# Python Packages - combinations and permutations
############################################################################################################
from itertools import permutations, combinations
# print(list(combinations(['a','b','b'], 2)))
# print(list(permutations(['a','b','c'], 3)))
# print(list(combinations(['a','b','c','d'], 3)))
# print(list(combinations(['a','b','c','d','e'],3)))

# arr = ['a','b','c']
# perm = [[x,y,z]for x in arr for y in arr for z in arr]

####
# [[abc], [acb],
#  [bac], [bca],
#  [cab], [cba]]

# permutations for each element in the array
# order matters
# the trick:
# f(bc) = b+f(c) + c+f(b)
# f(abc) = a+f(bc) + b+f(ac) + c+f(ab)

# also, be careful and perhaps do on paper how you will accumulate the items
# basically written for k = len(arr)
def perm(arr):
    if len(arr) ==0:
        return [[]]
    else: 
        res = []
        for i in range(len(arr)):
            x = arr[i]
            new_arr = arr[:i] + arr[i+1:]
            for y in perm(new_arr):
                z = [x] + y
                res.append(z)
        return res

# print(perm(['a','b','c',]))


#########################################################
### can you write permutations for n choose k?
# (1,2)
# 2 choose 1: 
# 1, 2

# 1,2,3
# 3 choose 2
# 1,2; 1,3; 2,1; 2,3; 3,1; 3,2'
# = 1+f(2 choose 1) + 2f(2 choose 1) + 1+f(2 choose 1)
# 1, 2
# 2 choose 2
# 12; 21

def permK(arr, k):
    if k ==1:
        return arr
    res = []
    for i in range(len(arr)):
        x = arr[i]
        new_arr = arr[:i] + arr[i+1:]
        for y in permK(new_arr, k-1):
            newPerm = x + y
            res.append(newPerm) 
    return res


arr = ['a','b','c']
print(permK(arr, 2))

