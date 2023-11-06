# isSubtree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
left = TreeNode(4)
leftTwo = TreeNode(1)
leftright = TreeNode(2)

right = TreeNode(5)

root.left = left
root.left.left = leftTwo
root.left.right = leftright
root.left.right.left = TreeNode(0)

root.right = right


sub = TreeNode(4)
sub.left = leftTwo
sub.right = leftright
sub.right.left = TreeNode(0)

# print(root.left == sub)

# print(sub == left)





# print([x.val for x in traverse(root)])
# print([x.val for x in traverse(sub)])
# searched = search(root, sub)
# print(searched)
# print([x.val for x in traverse(searched)])

def isSubtree(root, subRoot):
    def traverse(root):
        res = []
        if root:
            res.append(root)
            res = res + traverse(root.left)
            return res + traverse(root.right)
        else: 
            return res

    def search(root, subRoot):
        queue = traverse(root)
        res = []
        for x in queue:
            if x.val == subRoot.val:
                res.append(x)
        return res


    

    # searched_in_root = search(root, subRoot)
    # print('searched in root:')
    # print([x.val for x in searched_in_root])
    # subRoot_traverse = traverse(subRoot)
    # for x in searched_in_root:
    #     print('x: ')
    #     print(x.val)
    #     root_traverse = traverse(x)
    #     print([x.val for x in root_traverse])
    #     if (len(root_traverse) != len(subRoot_traverse)):
    #         continue
    #     if all([root_traverse[i] == subRoot_traverse[i] for i in range(len(subRoot_traverse))]):
    #         return True
    # return False    



def isSubtree(root, subRoot):
    # traverse 


x = TreeNode(1)
x.left = TreeNode(1)
y = TreeNode(1)

print(isSubtree(x, y))

