from bisect import bisect_left
def lengthOfLIS(nums):
    bucket = []
    parent = [-1]*len(nums)
    for i, num in enumerate(nums):
        if not bucket or num > nums[bucket[-1]]: 
            if not bucket: parent[i] = -1
            else: parent[i] = bucket[-1]
            bucket.append(i)
        else: 
            idx = bisect_left(bucket, num, key = lambda x: nums[x])
            parent[i] = bucket[idx-1]
            bucket[idx] = i
    return len(bucket)


nums = [1,4,9,2,5,3,7]
nums = [10,9,2,5,3,7,101,18]
nums = [1]
print(lengthOfLIS(nums))