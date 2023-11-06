
## longest increasing subsequence

from bisect import bisect



def lis(nums):
    res = [[nums[0]]]
    print(res)
    for x in nums[1:]:         
        index = bisect(res, x, key = lambda x: x[-1])        
        if index == 0: 
            insert = [x]
        else: 
            insert = res[index-1] + [x]
        if index == len(res):
            res = res + [insert]
            print('case 1')
        else: 
            res = res[:index-1] + [insert] + res[index:]
            print('case 2')
        print(res, 'index', index, 'x', x)
    return res[-1]

nums = [5,3,7, 9, 2, 1, 0, 11]

print(lis(nums))