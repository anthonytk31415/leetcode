def power(a,b):
    if b == 1: 
        return a
    if b % 2 == 0: 
        return power(a, b/2) * power(a, b/2)
    else: 
        return a * power(a, b/2) * power(a, b/2)
    

print(power(3, 8))