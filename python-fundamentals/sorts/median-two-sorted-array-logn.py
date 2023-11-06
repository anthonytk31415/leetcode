def findMedianSortedArrays(a, n, b, m):
    min_index = 0
    max_index = n

    while (min_index <= max_index):
        i = (min_index + max_index) // 2
        j = ((n + m + 1) // 2) - i

        if (i < n and j > 0 and b[j-1] > a[i]):
            min_index = i + 1

        elif (i > 0 and j < m and b[j] < a[i-1]):
            max_index = i - 1
    
        else: 
            if (i == 0):
                return b[j-1]
            if (j == 0):
                return a[i-1]
            else: 
                return max(a[i-1], b[j-1])
    print('error!')
    return -1

a = [1,3,5,7]
b = [2,4,6,8]
print(findMedianSortedArrays(a, len(a), b, len(b)))


z = a + b
z.sort()
print(z)
w = (z[len(z)//2] + z[len(z)//2 -1]) /2
print(w)