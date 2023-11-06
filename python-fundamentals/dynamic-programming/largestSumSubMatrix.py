



# dp[i][j] = (x,y)
# x = largest sum submatrix containing (i,j)
# y = largest sum sumatrix anywhere

# for each dp[i][j]:

# x = max(x from column above with new row added from row i with same k columns, 

#         )


# y = max(x for current (i,j), y from above)


# return dp[-1][-1][1] ## return bottom right dp, 1st index


def longestSubarray(arr):
    prefixSum = [x for x in arr]
    for i in range(1, len(prefixSum)):
        prefixSum[i] = prefixSum[i-1] + prefixSum[i]
    
    # longestInc is the longest subarray inclusive of i
    longestInc = [x for x in prefixSum]
    for i in range(1, len(longestInc)):
        longestInc[i] = max(arr[i], arr[i] + longestInc[i-1])
    
    # print(arr)
    # print(prefixSum)
    print(longestInc)
    return max(longestInc)

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# arr = [1,2,-4,1,-4,3,2,-1,2]
arr = [2,-3,4,9,-13, 3, -2, 4,5]

# arr = [5,4,-1,7,8]
# arr = [1,2, -4, 1, 3, -2, 4]
print(longestSubarray(arr))

