#lowest common ancestor

# concept: two things can happen: 
# - from the root, the two nodes can lie on the "same path", which means the node p will pass through node q to get to p via search (or the other way around)
# - or they each lie on separate paths. 
# - so we will "search" to find p. If we hit q along the way, return q. then do the same for p. 
# - then we will keep track of the route with an array.
# - at the end, if we dont hit any node, we'll traverse the smaller (by length) of the arrays to find the common node, starting from the 'bottom' (with the highest index)


# running time: worst case O(log n). You traverse through the depth of the tree 3 times


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# two = TreeNode(2)
# eight = TreeNode(8)
# four = TreeNode(4)
# root = TreeNode(6)
# root.left = two
# root.right = eight

# root.left.left = TreeNode(0)
# root.left.right = four
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)

# root.right.left = TreeNode(7)
# root.right.right = TreeNode(9)


def lowestCommonAncestor(root, p, q):
    route_p = []
    node = root
    while node.val != p.val: 
        if node.val == q.val:
            # print('win0')
            return q
        route_p.append(node)
        if p.val < node.val:
            node = node.left
        else: 
            node = node.right
    route_p.append(node)

    route_q = []
    node = root
    while node.val != q.val:
        if node.val == p.val:
            # print('win1')
            return p
        route_q.append(node)
        if q.val < node.val:
            node = node.left
        else: 
            node = node.right
    route_q.append(node)      

    print([x.val for x in route_p], [y.val for y in route_q])
    # traverse 
    if len(route_p) < len(route_q):
        route = route_p
        other_route = route_q
    else:
        route = route_q
        other_route = route_p
    for i in range(len(route) - 1,-1,-1):
        # print(route[i])
        if route[i] in other_route: 
            # print('win3')
            # print(route[i].val)
            return route[i]



## another answer: 
# if the start to diverge onto different paths, then one will be on the left of the node and one will be on the right, 
# so return that node, otherwise, keep traversing
# restated: if they're both < root: traverse left, if theyre both > root: traverse right, 
# otherwise return root immediately! beecause they are on divergent paths!!
def lowestCommonAncestor2(root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root


# print(lowestCommonAncestor(root, two, eight).val)

# print(lowestCommonAncestor(root, two, four).val)