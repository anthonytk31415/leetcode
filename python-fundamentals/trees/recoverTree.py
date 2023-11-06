# are all eleem


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root= TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)

def inorder(root, parent = None):
    res = []
    if not root: 
        return res
    else: 
        res = res + inorder(root.left, root)
        res.append((root.val, root, parent))
        return res + inorder(root.right, root)



    
# print(inorder(root))


def recoverTree(root):
    tree_list = inorder(root)
    nodes_to_swap = []
    print(tree_list)
    for i in range(len(tree_list)):
        if i == 0: 
            if not (tree_list[i][0] <  tree_list[i+1][0]):
                # print(tree_list[i][0])
                nodes_to_swap.append(tree_list[i]) 
        elif i < len(tree_list) - 1:
            if not (tree_list[i-1][0] < tree_list[i][0] <  tree_list[i+1][0]):
                nodes_to_swap.append(tree_list[i]) 
        else: # i == len(tree)-1:
            if not (tree_list[i-1][0] < tree_list[i][0]):
                nodes_to_swap.append(tree_list[i]) 

    ## you should have two nodes
    x_node, x_parent = nodes_to_swap[0][1], nodes_to_swap[0][2]
    y_node, y_parent = nodes_to_swap[1][1], nodes_to_swap[1][2]

    print(f'nodes to swap: {nodes_to_swap}')
    # if x_parent.val > y_node.val: 
    #     x_parent.right = y_node
    # elif x_parent.val < y_node.val: 
    #     x_parent.left = y_node

    # if y_parent.val > x_node.val: 
    #     y_parent.right = x_node
    # elif y_parent.val < x_node.val: 
    #     y_parent.left = x_node

    # x_node.left, x_node.right, y_node.left, y_node.right = y_node.left, y_node.right, x_node.left, x_node.right

    print(recoverTree(root))