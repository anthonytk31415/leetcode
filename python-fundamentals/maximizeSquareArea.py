def maximizeSquareArea(m, n, hFences, vFences):
    hFences= hFences + [m]
    vFences = vFences + [n]
    # hFences.sort(key = lambda x: -x)
    # vFences.sort(key = lambda x: -x)
    horiz = set()
    vert = set()
    for i in range(len(hFences)):
        horiz.add(abs(hFences[i] - 1))
        for j in range(0, i):
            horiz.add(abs(hFences[i] - hFences[j]))
    
    for i in range(len(vFences)):
        vert.add(abs(vFences[i] - 1))
        for j in range(0, i):
            vert.add(abs(vFences[i] - vFences[j]))


    horiz1 = list(horiz)
    horiz1.sort(key = lambda x: -x)
    for x in horiz1: 
        if x in vert: return (x**2) % (10**9 + 7) 
        
    return -1 

    # print( horiz, vert)

# m = 4
# n = 3
# hFences = [2,3]
# vFences = [2]

m = 3
n = 9
hFences = [2]
vFences = [8,6,5,4]


# m = 6
# n = 7
# hFences = [2]
# vFences = [4]

print(maximizeSquareArea(m,n, hFences, vFences))
