def dequeue(q):
    if len(q) == 0:
        return -1
    res = q[0]
    q = q[1:]
    return (res, q)

def adjacent(entry, x1, x2, y1, y2):
    (a,b) = entry
    return [(a + i, b) for i in [-1, 1] if i >= x1 and i <= x2] + [(a, b + j) for j in [-1,1] if j >= y1 and j <= y2] 

print(adjacent((0,0), 0,4,0,4))