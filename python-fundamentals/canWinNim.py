## if player 1 wins, player 0 loses

def canWinNim(n):
    cache = {1: True, 2: True, 3: True}
    
    if n <= 3: 
        return cache[n]
    for i in range(4, n+1):
        cache[i] = any([not cache[i-1], not cache[i-2], not cache[i-3]])

    return cache[n]

def canWinNim(n):
    if n % 4 == 0: 
        return False
    else:
        return True

print(canWinNim(7))

