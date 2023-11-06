from collections import Counter


# time: O(nlogn); O(n) for the count, nlogn for the sort

# def topKFrequent(nums, k):
#     countNums = Counter(nums)
#     numCount = sorted([(x, countNums[x]) for x in Counter(nums)], key = lambda z: -z[1])
#     return [numCount[i][0] for i in range(k)]


# even faster using the "counter" and "most_common" method 
# def topKFrequent(nums, k):
#     countNums = Counter(nums).most_common(k)
#     return [x[0] for x in countNums]

    # return [x[0] for x in numCount[:k]]


## Using quickselect
def topKFrequent(nums, k):
    countNums = Counter(nums)
    tuples = [(x, -countNums[x]) for x in countNums]
    
    def quickselect(tuples, p, r, k):
        if p < r: 
            q = partition(tuples, p,r)
            if q == p + (k-1):
                return p + (k - 1)
            elif q > p + (k - 1):
                return quickselect(tuples, p, q-1, k)
            else: 
                return quickselect(tuples, q+1, p + (k - 1) - q)

    def partition(tuples, p, r):
        pivot = tuples[r][1]
        i = p - 1
        for j in range(p, r):
            if tuples[j][1] < pivot:
                i +=1
                tuples[j], tuples[i] = tuples[i], tuples[j]
        tuples[r], tuples[i+1] = tuples[i+1], tuples[r]
        return i + 1

    index = quickselect(tuples, 0, len(tuples) -1, k)

    return [x[0] for x in tuples[:index + 1]]



nums = [1,1,1,2,2,3] 
k = 2

print(topKFrequent(nums, k))