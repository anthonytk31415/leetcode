arr = [1024,512,256,128,64,32,16,8,4,2,1]


# def sortByBits(arr): 

#     arrToSort = []
#     for num in arr: 
#         numOnes = 0
#         for char in bin(num)[2:]:
#             if char == '1': 
#                 numOnes += 1
#         arrToSort.append((numOnes, num))

#     arrToSort.sort(key = lambda x: (x[0], x[1]))


#     return [x[1] for x in arrToSort]



def sortByBits(arr):
    arr.sort(key=lambda x: (bin(x).count("1"), x))
    return arr

print(sortByBits(arr))

