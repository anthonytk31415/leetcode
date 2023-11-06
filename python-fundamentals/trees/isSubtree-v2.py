 
# Time: O(N*M) N nodes of root, M nodes of Subroot
# Space: O(1)

# this is the naive approach: 
def isSubtree(root, subRoot):
    def isEqual(node1, node2):
        if (not node1) and (not node2): 
            return True
        elif (not node1) or (not node2):
            return False
        elif node1.val == node2.val: 
            return True and isEqual(node1.left, node2.left) and isEqual(node1.right, node2.right)
        return False

    def findEqualNode(node1, node2):

        if not node1:
            return False
        else: 
            return isEqual(node1, node2) or findEqualNode(node1.left, node2) or findEqualNode(node1.right, node2)
        
    return findEqualNode(root, subRoot)

# faster solution: serialize
#  Solution 2: Serialize in Preorder then KMP

# string representation

# O(n^2) still since you're checking "in"
def isSubtree(root, subRoot):

    def stringRep(s):
        if not s: 
            return '#'
        else: 
            return '^' + str(s.val) + '$' + stringRep(s.left) + '$' + stringRep(s.right)
    
    s_root = stringRep(root)
    s_subroot = stringRep(subRoot)

    return s_subroot in s_root


# can use KMP algo after serializing to reduce to O(m+n)