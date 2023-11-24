# prefixSum

arr = [1,2,3,4,5,6]
prefixSum = [x for x in arr]
for i in range(1, len(arr)):
    prefixSum[i] = prefixSum[i] + prefixSum[i-1]

# sum of nums from i to j inclusive
def sumNumsInterval(i, j, prefixSum):
    if i == 0: 
        return prefixSum[j]    
    else: 
        return prefixSum[j] - prefixSum[i - 1]

# creating a monotonic increasing deque 
# property: d[-1] is smallest. 
d = ()
while d and d[-1] > cur: 
    d.pop()
d.append(cur)