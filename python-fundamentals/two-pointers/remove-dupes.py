
# 112213 --> 13
# 122213 --> 3
# remove the duplicates and return the length 

def removeDupes(arr):
    if len(arr) <= 1: 
        return len(arr)

    to_remove = 0           # counter to increase

    last_nondupe = None 
    found_dupe = False
    
    # when a dupe occurs    # keep track of the last non-deleted element so that when you get to ; a new char where the previous series got deleted
    for i in range(1, len(arr)):
        cur = arr[i]
        last_char = arr[i-1]
        
        if cur == last_char:
            found_dupe = True
            to_remove += 1

        else:
            if last_nondupe == cur: 
                to_remove +=1
                last_nondupe = None                
                found_dupe = True

            if found_dupe == True:
                to_remove += 1 
                found_dupe = False            

            last_nondupe = cur

    return len(arr) - to_remove



f

arr = ['a','b','c']

print(removeDupes(arr))

# for i, x in enumerate(arr):
#     print(i, x)

