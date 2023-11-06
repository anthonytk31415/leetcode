# start: 1:55 # end: 2:26

# Time: O(2^n * n ) since you are either keeping the element in the list of nums or not for all n 
# Space: O(2^n * n) will have possibly an entry for each iteration 

def findSubsequences(nums):
    res = set()

    def helper(nums, path, idx, res):
        # you reached the end of the nums
        if idx >= len(nums): 
            if len(path) >= 2 and tuple(path) not in res:
                res.add(tuple(path))
            return 
       
        else: 
            if len(path) >= 2 and tuple(path) not in res:       # add the pair or longer if not in res
                res.add(tuple(path)) 
            for i in range(idx, len(nums)):                     # note that initial step will start a "new chain" at each i
                if i > idx and nums[i] == nums[i-1]:            # skip over duplicates 
                    continue 
                if path == []:                                  # no path: continue
                    helper(nums, path + [nums[i]], i + 1, res)
                elif nums[i] >= path[-1]:                       # continue the path
                    helper(nums, path + [nums[i]], i + 1, res)
                else:                                           # next i is smaller than last path so go to next index
                    continue


    helper(nums, [], 0, res)
    return res

nums = [4,4,3,2,1]
# nums = [4,6,7,7]
print(findSubsequences(nums))