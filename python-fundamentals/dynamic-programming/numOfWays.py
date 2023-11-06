def numOfWays(n):
    same = 6
    diff = 6
    i = 1
    while i < n: 
        same, diff = same*3 + diff*2, same*2 + diff*2
        i += 1

    return (same + diff) % (10**9 + 7)


print(numOfWays(5000))

