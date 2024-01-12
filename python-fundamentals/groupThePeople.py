from collections import defaultdict

# O(N) Time and Space
# Maintain a hash map of the size and the group. input the person into the group of 
# appropriate size. When the group is full, move it to res, create a new group

def groupThePeople(groupSizes):
    res = []
    sizes = defaultdict(list)
    for i, size in enumerate(groupSizes):
        sizes[size].append(i)
        if len(sizes[size]) == size: 
            res.append(sizes[size]) 
            sizes[size] = []
    return res

groupSizes = [3,3,3,3,3,1,3]
groupSizes = [2,1,3,3,3,2]
print(groupThePeople(groupSizes))