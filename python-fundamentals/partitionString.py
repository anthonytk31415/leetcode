# use a greedy approach and make the longest chain you can. 

# Proof: Taking the longest current string possible means you have the shortest leftover.
# if you didn't take the longest string, then you would have more candidates to potentially make the 
# next strings require partitioning.

#Time: O(n); Space: O(n) for the set 

def partitionString(s):
    
    res = 0
    strTracker = set()
    i = 0
    while i < len(s):
    ## keep track of the current "path" w/ a set so you can keep track of the letters and new letters 
        if s[i] in strTracker: 
            strTracker = set()
            res +=1
        strTracker.add(s[i])
        i +=1
    res +=1
    return res

s = "ssssss"
print(partitionString(s))