# Time: O(nlogn)
# Space: O(n*k)


# this one is slow
def nthSuperUglyNumber1(n, primes):
    if n == 1: 
        return 1
        
    prime_set = set(primes)
    res = set()
    res.add(1)
    e = 1               # every time I find something, increase e by 1; 
    i = 2
    
    while e < n: 
        cur = i

        if i in prime_set: 
            res.add(i)
            e +=1

        else: 
            for p in primes: 
                if i % p == 0 and ((i / p) in res): 
                    res.add(i)
                    e +=1
                    break
        i +=1

    return cur



from heapq import heappush, heappop

def nthSuperUglyNumber(n, primes):
    if n == 1: 
        return 1
    queue = [1]
    counter = 1
    # visited = set()
    # visited.add(1)
    while counter <= n: 
        cur = heappop(queue)
        counter +=1
        for p in primes:
            # if cur * p not in visited: 
            #     visited.add(cur * p)
            heappush(queue, cur *p)
            if cur % p == 0: 
                break
    return cur


# n = 12
# primes = [2,7,13,19]

n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541]

print(len(primes))

print(nthSuperUglyNumber(n, primes))
