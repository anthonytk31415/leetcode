# Hash table implementation; 
# Create the map to find index of nums in O(1) time. Iterate through operations and swap the values as well as
# replacin gthe num to index with with new num old index and deleting old num. 

# #O(n) time and space

def arraychange(nums, operations):
    
    numToIndex = {}
    for i, num in enumerate(nums):
        numToIndex[num] = i
    
    for u, v in operations: 
        idx = numToIndex[u]
        nums[idx] = v
        del numToIndex[u]
        numToIndex[v] = idx
    
    return nums

nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]

nums = [1,2]
operations = [[1,3],[2,1],[3,2]]

print(arraychange(nums, operations))