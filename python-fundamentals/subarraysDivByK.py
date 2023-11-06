
# use prefix sum
# iterate over each i in nums
# if prefixSum % k is in the hash --> add n # of occurences to the counter; that means
#      there's been there are n subarrays up to i that are div by k
#
# keep a hash table to track prefixSum % k
# instantiate the hash with hash[0]=1

from collections import defaultdict

def subarraysDivByK(nums, k):
    counter = 0
    mod_counts = defaultdict(int)
    runningSum = 0 
    mod_counts[0] = 1
    for num in nums:
        runningSum += num
        cur_mod = runningSum % k
        if (cur_mod) in mod_counts:
            counter += mod_counts[cur_mod]
        mod_counts[cur_mod] +=1
    return counter

nums = [4,5,0,-2,-3,1]
k = 5

print(subarraysDivByK(nums, k))
