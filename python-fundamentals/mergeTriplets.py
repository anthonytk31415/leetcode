# Greedy algorithm: we get the answer with only 3 triplets: when some entry equals the target 
# entry and the others are <= target. If they are ever > target, we move on. 
# O(n) time, O(1) space

def mergeTriplets(triplets, target): 
    x, y, z = target
    res = [False]*3

    for a, b, c in triplets: 
        if a == x and b <= y and c <= z: res[0] = True
        if b == y and a <= x and c <= z: res[1] = True
        if c == z and a <= x and b <= y: res[2] = True
        if all(res): return True
    return False

triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
print( mergeTriplets(triplets, target))
