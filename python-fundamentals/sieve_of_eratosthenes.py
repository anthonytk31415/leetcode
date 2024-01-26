def sieve_of_eratosthenes(n):
    primes =  [True]*(n+1) 
    primes[0] = primes[1] = False
    for i in range(2, int(n**.5) + 1, 1):
        if primes[i]: 
            for j in range(i*i, n+1, i):
                primes[j] = False

    return [i for i in range(len(primes)) if primes[i]]

print(sieve_of_eratosthenes(50))