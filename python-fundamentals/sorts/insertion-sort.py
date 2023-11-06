# insertion-sort

def insertion_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and  a[j] > key:
            a[j+1] = a[j]
            j = j -1
        a[j+1] = key
    return a

a = [0,9,4,3,17,2]
insertion_sort(a)
print(a)