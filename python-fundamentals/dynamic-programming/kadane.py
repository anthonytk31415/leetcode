# kadane's largest subarray sum 

def kadane(arr):
    maxSum, prev, cur = 0, 0, 0

    for i, num in enumerate(arr):
        cur = max(prev + num, num)
        maxSum = max(maxSum, cur)
        prev, cur = cur, 0
    return maxSum

# arr = [1,-2,1]
arr = [1,2,-8, 1, 2, -1, 2]
print(kadane(arr))