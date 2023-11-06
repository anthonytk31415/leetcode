
def bagOfTokensScore(tokens, power):
    if not tokens: 
        return 0
    tokens.sort()
    i = 0
    j = len(tokens) - 1
    score = 0
    while i < j: 
        # print(i, j, score, power)
    # buy until you cannot; sell if that enables you to buy
        if power > tokens[i]:
            power -= tokens[i]
            score +=1
            i +=1

        elif score > 0 and (power + tokens[j] >= tokens[i]): 
            score -=1
            power += tokens[j]
            j -=1

        else: 
            break 

    # if there is only one element left, you either buy or you do nothing
    # print(i, j, score, power)
    if power >= tokens[i]:
        power -= tokens[i]
        score +=1
    
    return score

# tokens = [100]
# power = 50

# tokens = [100,200]
# power = 150

tokens = [100,200,300,400]
power = 200


print(bagOfTokensScore(tokens, power))