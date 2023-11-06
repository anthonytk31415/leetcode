# 9:11 8 min completion!

# trick: 
# - sort the list; keep track of the averge of
# - the pairs will always be the left most and right most
# - successively grab the left and rights; compare their average to ensure they are equal at each step
# - keep track of the cumulative "chemistry"


# n = length of skill
# - even length 
# skill array
# skill of ith player = skill

# divide into n/2 teams of size 2

# total skill equal 
# return chem of all teams 
# chemistry [team] = product of skills of players

# time = O(n*logn) 
# for the sort
# space = O(1)

def dividePlayers(skill):
    skill = sorted(skill) 
    l = 0
    r = len(skill) - 1
    chem = 0
    avg = (skill[l] + skill[r]) / 2

    while l < r: 
        if (skill[l] + skill[r]) / 2 != avg: 
            return -1
        chem = chem + skill[l]*skill[r]
        l +=1
        r -=1
    return chem