## getHint


def getHint(secret, guess):
    ## container for potential cows; 
    ## 'c': [a, b] --> c = char, a = secret occurances, b = guess occurances
    ## after cycling, z = # of bulls for given char; a = 7, b = 3 --> Z = 3; a = 0, b = 3, Z = 0 --> a = 2, b = 8, Z = 2; Z = min(a, b)
    cowContainer = {}
    bulls = 0
    ## check for bulls
    for i in range(len(secret)):
        s, g = secret[i], guess[i]
        if s == g:
            bulls +=1
        ## insert count of chars from guess and secret into the array
        else: 
            # assign secret occurances
            if s not in cowContainer: 
                cowContainer[s] = [1,0]
            else: 
                cowContainer[s][0] +=1
            # assign guess occurances
            if g not in cowContainer: 
                cowContainer[g] = [0,1]
            else: 
                cowContainer[g][1] +=1
    ## calculate cows
    cows = 0
    for key in cowContainer:
        a,b = cowContainer[key]
        cows = cows + min(a,b)
    return str(bulls) +'A' + str(cows) + 'B'

print(getHint('1807','7810'))
# print(getHint('1123','0111'))

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"