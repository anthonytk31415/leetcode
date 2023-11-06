# kth missing pos number

def findKthPositive(arr, k):
    lookup = set(arr)
    e = 0
    i = 1
    while e < k: 
        if i not in lookup:
            e +=1
            cur_not_found = i
        i +=1
    return cur_not_found

    
