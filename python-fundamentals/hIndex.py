def countingSort(a):
    b = [None]*len(a)
    c = [0]*(max(a)+1)

    for i in range(len(a)):
        c[a[i]]+=1

    for j in range(1, len(c)):
        c[j] = c[j] + c[j-1]

    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -=1
    return b[::-1]


a = [4,2,1,10,6,5,8]
print(countingSort(a))



def hIndex(citations):
    citations = countingSort(citations)
    i = 0
    n = len(citations)
    count = 0
    while n >= 0 and count < n:
        if citations[i] >= n:
            count +=1
            i +=1
        else: 
            n -=1
    return n        

# citations = [3,0,6,1,5]
citations = [1,3,1]
print(hIndex(citations))


# 1,2,3,4,5
# 0,1,3,5,6

# 5,5,3,1
# 6,5,3,1,0