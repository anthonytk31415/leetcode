# Write your code here.
def merge_sort(lst):
    print(f'list is: {lst}')
    import math
    if len(lst) <= 1:
        return lst
    r = len(lst) - 1
    q = math.floor((r - 0)/2)
    left_half = lst[0:q+1]
    right_half = lst[q+1:r+1]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    print(f'calling merge on : {left_half}, {right_half}')
    return merge(left_half, right_half)

def merge(left_half, right_half):
    # Merge logic goes here
    n_l = len(left_half)
    n_r = len(right_half)
    i = 0
    j = 0
    k = 0
    a = []
    while i < n_l and j < n_r:
        if left_half[i] <= right_half[j]:
            a.append(left_half[i])
            i +=1
        else:
            a.append(right_half[j])
            j +=1
        k +=1
    while i < n_l:
        a.append(left_half[i])
        i +=1
        k +=1
    while j < n_r:
        a.append(right_half[j])
        j +=1
        k +=1
    return a


lst = [5, 2, 38, 91, 16, 427]
print(lst)

sorted_lst = merge_sort(lst)        # Out of place solution
print(f'answer is: {sorted_lst}')

merge_sort(lst)                     # In place solution
print(lst)