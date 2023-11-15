class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def generateTrees(n):

    arr = [x for x in range(1, n + 1)]
    print(arr)
    def generateTreeFromSortedArray(arr):
        res = []
        if len(arr) == 0:
            return [None]

        for i, num in enumerate(arr):
            leftNodes = generateTreeFromSortedArray(arr[:i])
            rightNodes = generateTreeFromSortedArray(arr[i+1:])
            for leftNode in leftNodes:
                for rightNode in rightNodes:
                    parent = TreeNode(num)
                    parent.left = leftNode
                    parent.right = rightNode
                    res.append(parent)

        return res

    return generateTreeFromSortedArray(arr)


# print(generateTrees(2))


x = generateTrees(3)
print(x)
# print(x[1].val, x[1].left.val)
# print(x[0].val)