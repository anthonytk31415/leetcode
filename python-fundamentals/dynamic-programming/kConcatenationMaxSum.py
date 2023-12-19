


def kConcatenationMaxSum(arr, k):
    def kadane(arr):
        maxSum, prev, cur = 0, 0, 0

        for i, num in enumerate(arr):
            cur = max(prev + num, num)
            maxSum = max(maxSum, cur)
            prev, cur = cur, 0
        return maxSum


    if sum(arr) <= 0: return kadane(arr + arr)

    else: 
        return kadane(arr + [sum(arr)*(k-2)] + arr)

arr = [1,2] 
k = 3

arr = [1,-2,1] 
k = 5

print(kConcatenationMaxSum(arr, k))