# interview20221215
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# https://leetcode.com/problems/path-sum/


print('hello world')


arr = [1,2,4,5,6,7]
# assume all unique, come back and think about non-unique entries

class Node:
    def __init__(self): 
        self.val = None
        self.left = None
        self.right = None

    def balancedbinary(arr): 
        root = Node()

        ## write base cases
        if len(arr) ==0: 
            return 
        elif len(arr) == 1:
            root.val = arr[0]
        else:     
            median = (len(arr) - 0 )//2
            left = arr[0:median]
            right = arr[median + 1:len(arr)]

            root.val = arr[median]  ## val of 4
            root.left = Node.balancedbinary(left)
            root.right = Node.balancedbinary(right)

        return root

    def traversal(root):
        res = []
        if root: 
            res.append(root.val)
            res = res + Node.traversal(root.left)
            return res + Node.traversal(root.right)
        else: 
            return res

    ## given root of a tree, return root of cumulative sum tree
    def cumulativeSumTree(root):

        return root

    def search(root,)


a = [1,2,3,4,5,6,7]
## 4, 2, 1, 3, 6, 5, 7

root = Node.balancedbinary(a)
print(Node.traversal(root))




