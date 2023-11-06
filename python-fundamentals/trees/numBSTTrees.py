
#dynamic, memoization
#bottoms up to build the iteration tree
# - trick is to realize that for n nodes, you need one node at root, and then its a matter of calculating ways you can 
#   arrange (n-1 nodes on the right )*(0 nodes on the left) + (n-2 on right)*(1 on left) + (n-3 on right)*(2 on left)...
# - then you do bottoms up memoization for space purposes

# Time: O(n^2) calcs 
# Space: O(n) for memoization

# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def numTrees(n):
    track = {0: 1, 1: 1, 2:2} ## ways you can configure a k node tree
    if n <= 2:
        return track[n]

    for w in range(3,n+1):
        k = w-1
        # q = k//2
        inputs = []
        for i in range(0, k+1):             ## here's where you do n calcs over n loop so n^2 total calcs
            inputs.append((i, k-i))
        res = 0
        for z in inputs:         
            res = res + track[z[0]]*track[z[1]]
        track[w] = res
    print(track)
    return track[n]
    
print(numTrees(4))