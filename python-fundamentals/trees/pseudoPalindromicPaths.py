# We kind of build the solution in a backtracking/dfs fashion where at each node we add to a 
# counter the value and then recursively dfs to the child and at the end of the call, we remove that value. 
# When we get to a leaf node, we evaluate whether the counter represents a possible palindrome. 

# O(n) time to traverse each node with O(1) space to keep track of frequency of values from 1-9. 

from collections import Counter

def pseudoPalindromicPaths(root):
    counter = Counter()
    res = [0]

    def check():
        countOdd = 0
        for x in counter.keys(): 
            if counter[x] % 2 != 0: 
                countOdd += 1
                if countOdd > 1: return 
        res[0] += 1
        return 

    def dfs(node):
        counter[node.val] += 1
        if not node.left and not node.right: 
            check()
        for child in [node.left, node.right]:
            if child:
                dfs(child)

        counter[node.val] -= 1
    
    dfs(root)
    return res[0]