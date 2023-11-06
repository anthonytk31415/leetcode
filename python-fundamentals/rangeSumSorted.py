## Time: O(n**2) so
## Space: O(n!)

def rangeSum(nums, n, left, right):
    res = []
    cur_res = [x for x in nums]
    
    for i in range(1, len(nums)):
        cur_res[i] = cur_res[i] + cur_res[i-1]

    res = res + cur_res

    for _ in range(1, len(nums)):
        
        prior_res = [x for x in cur_res]
        cur_res = []
        key = prior_res[0]
        if len(prior_res) > 1: 
            for k in range(1, len(prior_res)):
                diff = prior_res[k] - key
                cur_res.append(diff)
        res = res + cur_res 
    
    res.sort()
    return sum(res[left-1:right]) % (10**9 + 7)

# nums = [1,2,3,4]
# n = 4
# left = 1
# right = 5


nums = [1,2,3,4]
n = 4
left = 3
right = 4

print(rangeSum(nums, n, left, right))