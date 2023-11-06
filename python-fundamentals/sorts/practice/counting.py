def countingSort1(a):
    b = [0]*len(a)                  # will contain the sorted output
    c = [0]*(max(a)+1)              # for ith entry of c, its the count of digit = i

    for i in range(len(a)):         # count the numbers in a
        c[a[i]]+=1

    for k in range(1, len(c)):      # make c[i] a rolling sum
        c[k] = c[k-1] + c[k]
    
    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]         # c[a[i]] -1 = index of where a[i] goes in b
        c[a[i]] -=1                 # reduce c[a[i]] for duplicate values

    return b



def countingSort(a):
    b = [0]*len(a)
    c = [0]*(max(a) + 1)

    for i in range(len(a)):
        c[a[i]] +=1
    
    for j in range(1, len(c)):
        c[j] = c[j-1] + c[j]

    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -=1

    return b

n = [1,3,2,8,5,6,2,3,8,4]
print(countingSort(n))