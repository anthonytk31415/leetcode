from heapq import heappush, heappop

def longestDiverseString(a, b, c):
    if a == b == c == 0: 
        return ""

    queue = []
    for num, char in [[a, "a"], [b, "b"], [c, "c"]]:
        if num > 0:
            heappush(queue, [-num, char])
    
    res, purgatory = [], []
    charStreak = 0

    curNum, curChar = heappop(queue)
    res.append(curChar)
    charStreak += 1
    curNum +=1
    if curNum < 0:
        heappush(queue, [curNum, curChar])

    while queue: 
        prevChar = res[-1]
        curNum, curChar = heappop(queue)

        if curChar == prevChar and charStreak == 2:
            purgatory.append([curNum, curChar]) 

        else: 
            if curChar == prevChar: 
                charStreak += 1
            else: 
                charStreak = 1
            res.append(curChar)
            curNum +=1
            if curNum < 0: 
                heappush(queue, [curNum, curChar])
            if purgatory: 
                purgNum, purgChar = purgatory.pop()
                heappush(queue, [purgNum, purgChar])
            
    return ''.join(res)

# a = 7 
# b = 1 
# c = 0

a = 1
b = 1 
c = 7
print(longestDiverseString(a, b, c))



# arr = [7,4,3,9,6,5,1,2,8]
# heap = []
# for x in arr: 
#     heappush(heap, x)

# print(heap)
# print(heap[0])

# arr1 = []
# print(arr1[-1])