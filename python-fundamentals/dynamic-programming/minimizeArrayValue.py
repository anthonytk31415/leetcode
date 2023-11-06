# dynamic programming  X nope too slow.
# you can go greedy!

# keep an average and dump as much as possible up to the average. 

# Time: O(n)
# space: O(1)

from functools import lru_cache

def minimizeArrayValue1(nums):
    nums_avg = int(sum(nums)/len(nums))
    # print(nums_avg)
    @lru_cache(None)
    def helper(nums, second, last, nums_avg):
        new_nums = tuple(nums[:-1])
        
        if last == 0 or last < nums_avg: 
            if not nums: 
                return second
            else: 
                return helper(new_nums, nums[-1], second, nums_avg)
        else: 
            res = []
            delta = 0
            for new_last in range(last, int(nums_avg)-1, -1):
                if not nums: 
                    input = second + delta
                else:
                    input = helper(new_nums, nums[-1], second + delta, nums_avg)
                cur_res = max(new_last, input)
                res.append(cur_res)
                delta +=1
            return min(res)

    res = helper(tuple(nums[:-2]), nums[-2], nums[-1], nums_avg)
    return res

from math import ceil
def minimizeArrayValue(nums):
    cur_sum = sum(nums)
    n = len(nums)
    nums_avg = cur_sum/n
    for i in range(len(nums)-1, 0, -1):
        delta = (nums[i] - ceil(nums_avg))
        # print('numsi: ', nums[i], '; avg: ', nums_avg, '; delta: ', delta)
        if delta > 0: 
            nums[i-1] += delta
            nums[i] -= delta
        cur_sum -= nums[i]
        n -=1   
        if delta <= 0: 
            nums_avg = cur_sum/n
    # print(nums)
    return max(nums)

# nums = [3,7,1,6] # --> avg = 4.25; at some point your avg up to where you are < global avg. nothing you can do. 
# nums = [13,13,20,0,8,9,9]
# nums = [439,228,482,150,231,209,991,125,453,407,670,491,300,125,285,749,350,411,527,768]
# nums = [97,777,495,796,192,606,6,667,792,119,275,241,277,404,983,775,206,147,422,377,
#         422,370,427,881,29,39,760,173,68,972,231,92,945,42,745,821,697,95,634,596,544,
#         780,167,329,811,908,764,536,633,270,48,540,323,743,844,92,423,176,693,785,535,
#         569,810,360,128,794,53,703,549]

nums = [4,7,2,2,9,19,16,0,3,15]

# print(sum(nums)/len(nums))
## maybe you iterate unitl you only get to the mid point

# for i - 1, ith position, 
# - delta = [ith position - avg]; if delta[i] > 0 that means it has too much and needs to get rid of it
# - if delta[i] <= 0, it has too little and can accept more from its right neighbor, (i+1)
# - so start from the far right: i and i+1; 
#     - if delta[i+1] > 0: it would like to give away delta 
#     - if delta[i+1] < 0, nothign you can do
#     - so the question is if delta[i+1] > 0, how much do you give away? 



# nums = [10,1]
print(sum(nums)/len(nums))
print(minimizeArrayValue(nums))


