def peakIndexInMountainArray(arr):

    left = 0
    right = len(arr) - 1
    while left <= right: 
        mid = (left + right) // 2
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid - 1] < arr[mid]:
            left = mid 
        else: 
            right = mid 

# arr = [0,1,2,3,4,3,2]
arr = [0,4,3,2,1]
arr = [0,1,2,3,4,5,6,5]
print(peakIndexInMountainArray(arr))