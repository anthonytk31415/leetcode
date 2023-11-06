# def longestCommonPrefix(strs):
#     container = ''
#     if len(strs) == 0:
#         return container
#     test = lambda x,y,i: x[0:i] == y[0:i] 
#     sortedList = sorted(strs, key = len)
#     # print(sortedList)
#     if len(strs[0]) == 0:
#         return container
#     for i in range(1, len(sortedList[0])+1):
#         check = sortedList[0]
#         if not all([test(x,check,i) for x in sortedList]):
#             return container
#         else: 
#             container = check[0:i]
#             print(container)
#     return container








def longestCommonPrefix(strs):
    container = ''
    if len(strs) == 0:
        return container
    test = lambda x,y,i: x[0:i] == y[0:i] 
    sortedList = sorted(strs, key = len)
    # print(sortedList)
    if len(strs[0]) == 0:
        return container
    for i in range(1, len(sortedList[0])+1):
        check = sortedList[0]
        if not all([test(x,check,i) for x in sortedList]):
            return container
        else: 
            container = check[0:i]
            print(container)
    return container





# strs = ["dog","racecar","car"]

# print(longestCommonPrefix(strs))
# print(len(longestCommonPrefix(strs)))
# strs2 = ["flower","flow","flight"]

strs2 = ["a"]

print(longestCommonPrefix(strs2))
# print(len(longestCommonPrefix(strs2)))