def minimumCost(arr):
    partial = arr[1:]
    partial.sort()

    return arr[0] + partial[0] + partial[1]


arr = [1,2,3,12]
# arr = [10,3,1,1]
print(minimumCost(arr))