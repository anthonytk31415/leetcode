## use the sieve of eratos

def countPrimes(n):
    if n < 2: 
        return 0
    primes = [True] *(n)
    primes[0] = primes[1] = False

    for i in range(2, n):
        if primes[i]:
            for j in range(i*2, n, i):
                primes[j] = False
    return sum(primes)


print(countPrimes(628545)) 

# def countPrimes(n):
#     if n <= 2:
#         return 0

#     primes = [True] * n
#     primes[0] = primes[1] = False 
    
#     for number in range(2, n):
#         if primes[number]:
#             for multiple in range(2 * number, n, number):
#                 primes[multiple] = False
                
#     #Sum of Total Booleans             
#     return sum(primes)