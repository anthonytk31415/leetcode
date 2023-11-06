def numFactoredBinaryTrees(arr):
    arr.sort()
    numTrees = {}
    numIdxLookup = set(arr)

    for i, num in enumerate(arr):
        trees = 1  # Each number can form at least one tree (itself).
        for j in range(i):
            divisor1 = arr[j]
            if num % divisor1 == 0:
                divisor2 = num // divisor1
                if divisor2 in numIdxLookup:
                    trees += numTrees[divisor1] * numTrees[divisor2]

        numTrees[num] = trees

    totalTrees = sum(numTrees.values())  # Sum up the number of trees for all numbers in arr.
    return totalTrees % (10**9 + 7)

# arr = [2,4,5,10]
# arr = [2,3,6,36]

arr = [45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]
print('ans', numFactoredBinaryTrees(arr))


