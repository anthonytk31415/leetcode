
# there are at least nodes= sum of 2**0 + 2**1 + ... + 2**(d-1) 
# we now find the nodes in the last depth

# traverse all the way left to find the depth
# then go right once and left depth-1 times. if a node exists, then 
# call the function recursively on root.right and add 2**(depth-1) to the answer; reduce depth by one
# else call the function recursively on root.left; reduce depth by 1


# Time: O(logn * logn) - you go logn each time you call the function and you do binary search on the 
# last depth so you traverse logn * logn times.
# Space: O(1)


from collections import deque


def countNodes(root):
    if not root:
        return 0
    depth = 0
    node = root
    while node and node.left: 
        node = node.left
        depth +=1
    
    sum_before_leaves = 0
    for x in range(depth):
        sum_before_leaves += 2**x

    def search(root, depth):
        if depth == 0:
            return 1
        node = root.right
        for _ in range(depth - 1):
            node = node.left
        if node: 
            return 2**(depth-1) + search(root.right, depth -1)
        else: 
            return search(root.left, depth - 1)
    
    return search(root, depth) + sum_before_leaves