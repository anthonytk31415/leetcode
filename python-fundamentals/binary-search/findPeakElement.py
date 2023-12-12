# Time O(nlogn); Space: O(1)
from math import inf

def findPeakElement(nums):
    nums = [-inf] + nums + [-inf]
    left = 0
    right = len(nums) - 1
    while left <= right:    
        mid = (left + right) // 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid - 1        
        if nums[mid] > nums[mid - 1]:
            left = mid
        else: 
            right = mid

# here's the 2D version. 
# Intuition: 

# Instantiate with minRow = 0, maxRow = len(mat)-1. We find the global max of a given row. 
# Then look at its column neighbors. If they're all smaller than the global max of the row, 
# then we have a 2D Peak. If not, take the side with the neighbor > global max of a given row. 
# Why? Because that neighbor is larger than everything in the given row. And in the neighbor's
# when you find its global max, that will be larger than everything in the prior row. 
# So we can cut the matrix in half each time using this logic. 

# Formally, if mat[mid][globalMaxJ] < mat[mid][globalMaxJ - 1]:
# left = mid
# else: right = mid

# In this setup, we also do the trick where we attach the whole matrix with -inf's around the perimeter: 
# mat = [[-inf]*(len(mat[0]) + 2)] + [[-inf] + row + [-inf] for row in mat] + [[-inf]*(len(mat[0]) + 2)] 

# O(n log m) Time; Space = O(1)

def findPeakGrid(mat):
    def linearMax(arr):
        arrMax = -inf
        idxMax = -1
        for i, num in enumerate(arr): 
            if num > arrMax:
                arrMax = num
                idxMax = i
        return idxMax

    mat = [[-inf]*(len(mat[0]) + 2)] + [[-inf] + row + [-inf] for row in mat] + [[-inf]*(len(mat[0]) + 2)] 
    rowMin = 0
    rowMax = len(mat) - 1
    while rowMin <= rowMax:
        mid = (rowMin + rowMax) // 2
        colMax = linearMax(mat[mid])
        if mat[mid][colMax] > mat[mid + 1][colMax] and mat[mid][colMax] > mat[mid - 1][colMax]:
            return [mid - 1, colMax - 1]
        if mat[mid][colMax] < mat[mid + 1][colMax]:
            rowMin = mid
        else: 
            rowMax = mid 
    return -1

    # return [resRow, resCol]

mat = [ [48,36,35,17,48],
        [38,28,38,26,24],
        [15, 9,33,32, 6],
        [49, 4, 8,10,41]]

# mat = [[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11]]

# mat = [ [2 ,1 ,99,98,22,21,20],
#         [3 ,2 ,1 ,2 ,3 ,4 ,19],
#         [4 ,3 ,2 ,1 ,2 ,3 ,18],
#         [5 ,4 ,3 ,2 ,1 ,2 ,17],
#         [6 ,5 ,4 ,3 ,2 ,1 ,16],
#         [7 ,6 ,5 ,4 ,3 ,2 ,15],
#         [8 ,9 ,10,11,12,13,14]]

# mat = [[10,20,15],[21,30,14],[7,16,32]]
print(findPeakGrid(mat))


# nums = [5,6,5, 8, 3, 2, 4, 1, 0]
# print(findPeakElement(nums))