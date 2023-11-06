# Counting Sort

# sort numbers/chars ranging from 0 to k
# a - array of numbers 

# def counting_sort(a,k): 
#     b = [0]*len(a)              # 
#     c = [0]*(k+1)               # c will contain the cumulative occurences 
#     for j in range(len(a)):
#         c[a[j]] +=1             # c[j] is the count of digit j 
#     for i in range(1,k+1):
#         c[i] = c[i] + c[i-1]    # now c[j] is the cumulative count; 
#                                 # c[j] means value at index j goes to position c[j] - 1 in b
#     for j in range(len(a)-1, -1, -1):
#         b[c[a[j]]-1] = a[j]     # 
#         c[a[j]] -=1             
#     return b

# def counting_sort1(a,k): 
#     b = [0]*len(a)
#     c = [0]*(k+1)
#     for i in range(len(a)):
#         c[a[i]] +=1
#     for j in range(1, len(c)):
#         c[j] = c[j] + c[j-1]
#     for i in range(len(b)-1, -1, -1):
#         b[c[a[i]]-1] = a[i]
#         c[a[i]] -=1
#     return b

    
# def counting_sort(a,k):
#     b = [0] * len(a)
#     c = [0] * (k+1)
#     for j in range(len(a)):
#         c[a[j]] +=1
#     for i in range(1, len(c)):
#         c[i] = c[i] + c[i-1]
#     for j in range(len(a)-1, -1, -1):
#         b[c[a[j]]-1] = a[j]
#         c[a[j]] -=1
#     return b


# def counting_sort(a,k):
#     b = [0]*len(a)
#     c = [0]*(k+1)
#     for j in range(len(a)):
#         c[a[j]]+=1
#     for i in range(1, len(c)):
#         c[i] = c[i] + c[i-1]
#     for j in range(len(a)-1, -1, -1):
#         b[c[a[j]]-1] = a[j]
#         c[a[j]] -=1
#     return b

# each element in a[i] has d digits from digit 1 to digit d: 

def counting_sort(a,k,exp):
    b = [0] * len(a)
    c = [0] * (k + 1)
    for j in range(len(a)):
        index = int((a[j]/exp)%10)
        c[index] +=1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i-1]
    for j in range(len(a)-1, -1, -1):
        index = int((a[j]/exp)%10)
        b[c[index] - 1] = a[j]
        c[index] -=1

    a = [x for x in b]
    print(a)

def radix_sort(a):
    max_a = max(a)
    exp = 1
    while max_a/ exp > 0: 
        counting_sort(a, 10, exp)
        exp *=10



a = [201,532,312,131,981,300,609,993]

# a = [2,5,3,0,2,3,0,3]
print(radix_sort(a))
print(a)
# j = 7
# a[7] = 3
# c[3] = 7
# b[7] = 3
