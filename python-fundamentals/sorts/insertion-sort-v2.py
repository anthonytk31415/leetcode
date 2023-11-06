# insertion sort


# def insertionSort(a):
#     for i in range(1,len(a)):
#         key = a[i]
#         print(i, key)
#         j = i - 1
#         while j >= 0 and key < a[j]:
#             a[j+1] = a[j]
#             j -=1
#         a[j+1] = key

# # a = [4,1,6,7]
# a = [4,1,6,7,3,8,2,5]
# insertionSort(a)

# print(a)


def insertionSort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -=1
        a[j+1] = key


a = [4,1,6,7,3,8,2,5]
insertionSort(a)
print(a)