# https://leetcode.com/problems/permutations-ii/
# permuteUnique

from collections import defaultdict

# time = O(n!)
# space: O(n!)

def permuteUnique(nums):
    lookup = defaultdict()
    for i in set(nums):
        lookup[(i,)] = [[i]]

    def helper(nums, lookup):
        nums = tuple(sorted(nums))
        if nums not in lookup:
            res = []
            for i in range(len(nums)):
                x = nums[i] 
                complement = nums[:i] + nums[i+1:]
                for c in helper(complement, lookup):
                    z = [x] + c
                    if z not in res: 
                        res.append(z)
            lookup[nums]=res            
        

        return lookup[nums] 

    return helper(nums, lookup)

print(permuteUnique([1,1,2]))


# check out backtracking for permutations
# https://leetcode.com/problems/permutations-ii/solutions/189116/summarization-of-permutations-i-and-ii-python/?orderBy=most_votes