# overlapping intervals 


# def merge_intervals(arr):
#     arr.sort(key = lambda x: x[0])
#     index = 0

#     for i in range(1, len(arr)):
#         ## merge intervals criteria: 
#         if arr[index][1] >= arr[i][0]: 
#             arr[index][1] = max(arr[index][1], arr[i][1])
#         else: 
#         # move index up one to retain; copy the ith spot into the index + 1 slot to prepare that one to be merged to the next i if needed
#             index = index + 1
#             arr[index] = arr[i]
#     arr = list(arr[:index+1])
#     return arr

def merge_intervals(arr):
    arr.sort(key = lambda x: x[0])
    index = 0
    for i in range(1, len(arr)):
        if arr[index][1] >= arr[i][0]:
            arr[index][1] = max(arr[index][1], arr[i][1])
        else: 
            index +=1
            arr[index] = arr[i]
    arr = arr[:index+1]
    return arr



# def mergeIntervals(arr):
 
#     # Sorting based on the increasing order
#     # of the start intervals
#     arr.sort(key=lambda x: x[0])
 
#     # Stores index of last element
#     # in output array (modified arr[])
#     index = 0
 
#     # Traverse all input Intervals starting from
#     # second interval
#     for i in range(1, len(arr)):
 
#         # If this is not first Interval and overlaps
#         # with the previous one, Merge previous and
#         # current Intervals
#         if (arr[index][1] >= arr[i][0]):
#             arr[index][1] = max(arr[index][1], arr[i][1])
#         else:
#             index = index + 1       #
#             arr[index] = arr[i]     # 
 
#     print("The Merged Intervals are :", end=" ")
#     for i in range(index+1):
#         print(arr[i], end=" ")
 

# a = [[6, 8], [1, 9], [2, 4], [4, 7], [10, 13], [11, 15]]
a = [[1,4],[0,2],[3,5]]
print(merge_intervals(a))

print(a)