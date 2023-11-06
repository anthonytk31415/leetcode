# k strongest

# sort arr
# define median
# 
# set left, right to 0, len(arr) - 1
# do the comparison and append to teh answer


def getStrongest(arr, k):
    arr.sort()
    med_idx = (len(arr)-1 - 0)//2
    median = arr[med_idx]
    res = []
    left, right = 0, len(arr) - 1
    while len(res) < k:
            if abs(arr[left] - median) < abs(arr[right] - median):
                res.append(arr[right])
                right -=1
            elif abs(arr[left] - median) > abs(arr[right] - median):
                res.append(arr[left])
                left +=1
            # condition where theyre equal
            else: 
                if arr[left] > arr[right]:
                    res.append(arr[left])
                    left +=1
                else: 
                    res.append(arr[right])
                    right -=1
    return res

# arr = [1,2,3,4,5]
# k = 2

arr = [6,7,11,7,6,8]
k = 5

# [6, 6, 7, 7, 8, 11]
# median = 7

print(getStrongest(arr, k))