# search 2d matrix


# first make a matrix for each row of the n-1th (last) entry; this is the largest
# time = O(logn + logm)
# 1 2 3 4


#3x2
# m = 3; n = 2
# low = 0
# high =  5 = 3 * 2 - 1 = m *n - 1
mid = (low + high) / 2 = 5/2 = 2.5
mid/cols = 2.5/2



def searchMatrix(matrix, target):
    for x in matrix:
        if target in x:
            return True
    return False


def searchMatrix(matrix, target):
    if len(matrix) == 1:
        return target in matrix[0]
    q = len(matrix)//2
    n = len(matrix[0])
    if target <= matrix[q-1][n-1]:
        return searchMatrix(matrix[:q], target)
    else: 
        return searchMatrix(matrix[q:], target)


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(searchMatrix(matrix, 23))