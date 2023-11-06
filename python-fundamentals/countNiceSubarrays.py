def numberOfSubarrays0(nums, k):

    # build number of odds, then cumulative
    odds = [0]*len(nums)
    for i in range(len(nums)):
        if nums[i] % 2 == 1: odds[i] = 1
    # print(odds)
    for i in range(1, len(nums)):
        odds[i] = odds[i] + odds[i-1]

    # then build array of arrays with [num_odds, qty] = ith entry
    cur = [0, 1]        # instantiate with the empty array for when odds = 3
    odds_compressed = []
    len_oc = 0
    j = None
    for i in range(len(odds)):
        if j == None and odds[i] >= k:      # first time you arrive at i where j needs to go; 
            j = len_oc + 1                  # watch you you haven't appended j yet
        if odds[i] == cur[0]:       
            cur[1] +=1
        else: 
            len_oc +=1
            odds_compressed.append(cur)
            cur = [odds[i], 1]

    if j == None: 
        return 0
    len_oc +=1
    odds_compressed.append(cur)
    i = 0
    # then set pointers j at first k or higher, i = 0. 
    # when arr[j][0] - arr[i][0] == k: count += arr[j][1] * arr[i][1]
    # then j +=1, i +=1
    # do until j > len or j >= i
    res = 0
    while j < len(odds_compressed):
        if odds_compressed[j][0] - odds_compressed[i][0] == k: 
            res += odds_compressed[j][1] * odds_compressed[i][1]
            i +=1
            j +=1
        elif odds_compressed[j][0] - odds_compressed[i][0] > k: 
            i +=1
        else: 
            j +=1
    return res

from collections import defaultdict

def numberOfSubarrays(nums, k):

    countOdds = 0
    prefix = defaultdict(int)
    prefix[countOdds] +=1
    for i in range(len(nums)):
        if nums[i] % 2 == 1: 
            countOdds +=1
        prefix[countOdds] +=1

    res = 0
    for c in prefix:
        if c - k in prefix:
            res += prefix[c] * prefix[c - k]
    return res


# nums = [1,1,2,1,1]
# k = 3
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

print(numberOfSubarrays(nums, k))




def subarraySum(nums, k):
    curSum = 0
    prefix = defaultdict(int)
    prefix[curSum] +=1
    res = 0
    for x in nums: 
        curSum += x
        if curSum - k in prefix: 
            res += prefix[curSum - k]
        prefix[curSum] +=1
    return res


# nums = [1]
# k = 0

# m

# nums = [-1,-1,1]
# k = 1
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(subarraySum(nums, k))