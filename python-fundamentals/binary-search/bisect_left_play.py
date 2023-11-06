from bisect import bisect_left, bisect_right, bisect

a = [0,1,2,2,2,3]
print('bisect left: ', bisect_left(a, 2))
print('bisect right: ', bisect_right(a, 2))
print('bisect: ', bisect(a, 2))


# can be used with list.insert() to properly insert the value but note the O(n) operation on insert
a.insert(bisect_left(a,2), 2)
print(a)


# longest increasing subsequence: 
# the patience sorting algorithm: 
# - keep track of a side array. call this bucket
# - initiate with putting the first element of your target arr in the bucket
# - now iterate i from left to right of the arr :
#     - if the current ith number > the last element of bucket: append ith to bucket
#     - otherwise, idx = binary search index for the smallest number larger than ith and 
#       replace bucket[idx] = ith 
# - return length of bucket



def lis(arr):
    if len(arr) <= 1: 
        return len(arr)

    res = 1
    path = [arr[0]]
    for i, num in enumerate(arr[1:]):
        if num > path[-1]:
            path.append(num)
            res += 1
        else: 
            idx = bisect_left(path, num)
            path[idx] = num
    return res


print(lis([1,10, 5, 3, 2, 9, 27, 6, 7, 8]))



def powersFour(): 
    res = set()
    for i in range(-32, 32):
        res.add(4**i)
    return res

# print(powersFour())