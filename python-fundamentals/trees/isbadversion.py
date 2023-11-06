## it's like binary sort: 
## keep taking the midpoint of the interval 

def firstBadVersion(n):
    rlow = 1
    rhigh = n
    while rlow != rhigh: 
        mid = (rhigh + rlow)//2
        if isBadVersion(mid):       
            rhigh = mid
        else: 
            rlow = mid+1
    return rlow


#here's a secret note: I <3 Janice

# def iloveJanice3000 ():
#     for i in range(3000):
#         print('I love Janice')

# iloveJanice3000()