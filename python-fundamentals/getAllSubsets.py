
# classic method of getting all subsets of n objects (from 0, 1, ... n-1) using recursion

def getAllSubsets(n):
    subset = []
    res = []
    def getSubsets(k):
        if k == n: 
            res.append([x for x in subset])
        else: 
            getSubsets(k + 1)
            subset.append(k)
            getSubsets(k + 1)
            subset.pop()
    getSubsets(0)
    return res

n = 3
print(getAllSubsets(n))


# Perhaps a more pythonic way, no explicit recursion with functions but utilizes previous state. 
# Initialize with them empty set. For each i, our resultant set is the previous res and for each element in the res, we 
# append i. 

def getAllSubsets1(n): 
    res = [[]]

    for i in range(n):
        res = res + [x + [i] for x in res]
    return res

n = 3
print(getAllSubsets1(n))

