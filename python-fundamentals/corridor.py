# SS PP SPS PP SS 
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/



# count two S. Then mark 1 way. Then add to "ways" number of subsequent trees before next chair
# how is this a hard? 
# Time: O(n); Space: O(1)

from collections import Counter
def numberOfWays(corridor):
    counts = Counter(corridor)
    if "S" not in counts: 
        return 0
    if counts["S"] %2 != 0: 
        return 0
    
    res = 1

    curS = 0 
    ways = 0 
    for char in corridor:
        if curS == 2: 
            if char == "S":
                res *= ways
                ways = 0
                curS = 1
            if char == "P":
                ways += 1
        else: 
            if char == "S":
                curS += 1
            if curS == 2: 
                ways += 1
    return res % (10**9 + 7)

             
corridor = "SSPPSPS"
# corridor = "PPSPSP"
corridor = "SSSSSSSPPPPP"
5,4,6
corridor = "SSPPPPSPPSPPPSSSSPPPPP"

print(numberOfWays(corridor))