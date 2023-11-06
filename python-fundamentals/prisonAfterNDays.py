from functools import lru_cache

def prisonAfterNDays(cells, n):
    cells = tuple(cells)
    lookup = set()         # cells = 1st, cycle 

    def next(cells):
        res = [0] * len(cells)
        for i in range(1, len(cells) - 1): 
            if cells[i-1] == cells[i+1]:
                res[i] = 1
            else: 
                res[i] = 0
        return tuple(res)

    count = 0
    hasCycle = False
    for _ in range(n): 
        cur_res = next(cells)
        if cur_res not in lookup:
            lookup.add(cur_res)
            count +=1
        elif cur_res in lookup: 
            hasCycle = True
            break
        cells = cur_res
    if hasCycle: 
        n = n % count
        for _ in range(n):
            cells = next(cells)

    return cells

cells = [0,1,1,1,0,0,0,0]
n = 99
# cells = [1,0,0,1,0,0,1,0]
# n = 1000000000
print(prisonAfterNDays(cells, n))