# binary tree level order traversal
# build a container 'res' and put the current layer in there, i.e. 
# all the vals of each layer
# then create a new layer of children nodes and do it again. 
# stop when the children nodes are empty

def levelOrder(root):
    res = []
    nodes = [root]
    while any(nodes):
        parents = [x.val for x in nodes if x]
        res.append(parents)
        children = []
        for x in nodes:
            if x.left: children.append(x.left)
            if x.right: children.append(x.right)
        nodes = children
    return res