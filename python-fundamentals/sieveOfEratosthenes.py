### interesting algo here: sieve of eratosthenes
### returns list primes less than n 
def sieve(n):
    res = [True] * (n + 1) ## values accepted for 2 to n
    primes = []
    for p in range(2, n+1): 
        if res[p] == True: 
            primes.append(p)
            j = 1
            while p*j <= n: 
                res[p*j] = False
                j +=1
    return primes