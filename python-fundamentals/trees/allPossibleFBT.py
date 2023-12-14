class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# here's like a DP solution. can we write this iteratively? 

def allPossibleFBT(n):
    res = {1: [TreeNode(0)]}
    if n % 2 == 0: return []
    for i in range(3, n+1, 2):
        print(i)
        curRes = []
        for j in range(1, i, 2):       
            leftCandidates = res[j]
            rightCandidates = res[i - j-1]
            for left in leftCandidates: 
                for right in rightCandidates:
                    newNode = TreeNode(0)
                    newNode.left, newNode.right = left, right
                    curRes.append(newNode)
        res[i] = curRes

    return res[n]

print(allPossibleFBT(7))