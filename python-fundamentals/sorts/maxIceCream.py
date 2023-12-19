def countingSort(a):
    k = max(a)

    b = [0] * len(a)
    c = [0] * (k + 1)
    
    for i in range(len(a)):
        c[a[i]] += 1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i-1]
    for j in range(len(a) - 1, -1, -1):
        b[c[a[j]] - 1] = a[j]
        c[a[j]] -=1 
    return b 

a = [1,4,3,2,5, 8]

print(countingSort(a))


def maxIceCream(costs, coins):

    # counting sort is basically storing frequencies of the index
    def countingSort(a):
        k = max(a)              # idx of c = frequency of index
        b = [0] * len(a)        # result = b
        c = [0] * (k + 1)       # 0th element for cumulative purposes
        
        for i in range(len(a)):
            c[a[i]] += 1
        for i in range(1, len(c)):  #apply cumulative
            c[i] = c[i] + c[i-1]
        for j in range(len(a) - 1, -1, -1):
            b[c[a[j]] - 1] = a[j]           # start w/ largest idx; work backwards
            c[a[j]] -=1                     # decrement c
        return b 

    sortCosts = countingSort(costs)
    cones = 0
    for i in range(len(sortCosts)):
        if sortCosts[i] <= coins: 
            cones += 1
            coins -= sortCosts[i]
        else: break
    return cones

costs = [1,3,2,4,1]
coins = 7
print(maxIceCream(costs, coins))