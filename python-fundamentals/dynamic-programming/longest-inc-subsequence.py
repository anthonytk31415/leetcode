## given arr and x, find index i of the spot where 
def binary_search_index_insert(arr, x, p, r):
    if p == r: 
        if arr[p] < x: 
            return p + 1
        else: 
            return p  
    else: 
        q = (p + r) // 2
        if arr[q] > x: 
            return binary_search_index_insert(arr, x, p, q-1)
        elif arr[q] < x: 
            return binary_search_index_insert(arr, x, q+1, r)
        elif arr[q] == x:
            return q




arr = [0,1,2,3,4,5,6,7]
x = 6.9
# idx = binary_search_index_insert(arr, x, 0, 7)
# print('new index: ', idx)
# arr.insert(idx, x)                              ## list.insert(index, object)
# print(arr)
from bisect import bisect_left




## returns insertion point index i in arr where x should go to maintain the sorted order
## ready to use list.insert() 
idx = bisect_left(arr, x)
print(idx)
arr.insert(idx, x)                              ## list.insert(index, object)
print(arr)

# Overall Strategy: keep an array of "min substring" with subs; append when cur > subs[-1]; replace at subs[j] to maintain smallest
# - instantiate with sub = [nums[0]]
# - iterate over nums range(1:)
# - if nums[i] > sub[-1]: append to sub; 
# - otherwise, find j of subs where sub[j-1] < nums[i] < sub[j+1] -- replace the current j with nums[i]
#       - subs will always be increasing/sorted --> we can binary search (Time: O(nlogn)) 
# - Notice you always keep the max length of the current incr. substring 
#   length but also replace the jth position with the smallest possible member in that "rank" ; 
# - When new i's get discovered they can potentially fill that next "increasing" chained spot and take over the overall chain


def lengthOfLIS(nums):
    if len(nums) <= 1: 
        return len(nums)

    subs = [nums[0]]
    for i in range(1, len(nums)):
        # print(subs, nums[i])
        if nums[i] > subs[-1]: 
            subs.append(nums[i])
        else: 
            idx = bisect_left(subs, nums[i])
            subs[idx] = nums[i]

    return subs
nums = [20,0,10,6,11,2,3,5]
print(lengthOfLIS(nums))

from bisect import bisect 

def path_lis(nums):
    sub, subindex, trace = [], [], [-1]*len(nums)
    for i, x in enumerate(nums):
        if len(sub) == 0 or x > sub[-1]:
            if subindex:
                trace[i] = subindex[-1]
            sub.append(x)
            subindex.append(i)
        else: 
            idx = bisect(sub, x)
            if idx > 0: 
                trace[i] = subindex[idx - 1]
            sub[idx] = x
            subindex[idx] = i
    path = []
    t = subindex[-1]
    while t >= 0: 
        path.append(nums[t])
        t = trace[t]
    return path[::-1]

print(path_lis(nums))