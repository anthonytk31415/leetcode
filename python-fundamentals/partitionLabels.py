# Time: O(n) 
# Space: O(1) since there are only a constant number of characters
# key is to merge intervals

def partitionLabels(s):

    intervals = {}
    for i in range(len(s)):
        if s[i] not in intervals: 
            intervals[s[i]] = [i, i]
        else: 
            intervals[s[i]][1] = i

    # find overlapping intervals
    arr = [intervals[x] for x in intervals]
    arr.sort(key=lambda x: x[0])
    index = 0
    for i in range(1, len(arr)):
        if arr[index][1] >= arr[i][0]:
            arr[index][1] = max(arr[index][1], arr[i][1])
        else: 
            index+=1 
            arr[index] = arr[i]
    arr = arr[:index+1]
    
    return [(x[1]-x[0]+ 1) for x in arr]


s = "ababcbacadefegdehijhklij"

print(partitionLabels(s))