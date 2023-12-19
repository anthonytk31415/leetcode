
# you can probably do this in one fell swoop. 
# along the way, make a parent array that points to the node's parent
# dfs from the root. 
# if the node == to_delete: 
# - remove that node from its parent
# - append that node's children to the res 

def delNodes(root, to_delete):
    parent = {root.val: -1}
    to_delete = set(to_delete)
    res = set([root])

    def dfs(node):
        if node.val in to_delete: delete(node)
        for child in [node.left, node.right]:
            if child: 
                parent[child.val] = node 
                dfs(child)

    def delete(node):
        # delete from parent
        nodeParent = parent[node.val]
        if nodeParent != -1: 
            if nodeParent.left == node: nodeParent.left = None
            if nodeParent.right == node: nodeParent.right = None
        # for each child of parent: append child to res; update child's parent to -1 
        for child in [node.left, node.right]:
            if child: 
                parent[child.val] = -1
                res.add(child)

        if node in res: res.remove(node)
        return 
    
    dfs(root)
    return res

# a = set()
# a.add(1)
# a.add(2)
# a.remove(1)
# print(a)