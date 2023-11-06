# base binary search

# this takes Time: log n

def binarySearch(arr, key):
    

    def helper(arr, key, i, j):
        print(i, j)
        if i > j: 
            return False
        if i == j:
            if arr[i] == key: return j
            else: return False

        mid = (i + j )// 2
        if key == arr[mid]: return mid
        if key < arr[mid]: 
            return helper(arr, key, i, mid - 1)
        else: 
            return helper(arr, key, mid + 1, j)


    return helper(arr, key, 0, len(arr) - 1)




## rewrite this using iterative

def binarySearch(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right: 
        mid = (left + right) // 2
        if key == arr[mid]: return mid
        elif key < arr[mid]: 
            right = mid -1
        else: 
            left = mid + 1              # this will push you out of the boundary and exit to the False condition if your key is not in the arr
    return False


arr = [0,1,2,3,4,5,6,9]
# arr = [0,1,4,6] 
key = 4

print(binarySearch(arr, key))