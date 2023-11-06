class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque

def cloneGraph(node):
    if not node: 
        return

    d = {node:Node(node.val)}
    stack = deque()
    stack.append(node)
    while stack: 
        cur = stack.popleft()
        # get children from stack
        for child in cur.neighbors:
            d[cur].neighbors.append(d[child])
            if child not in d: 
                d[child] = Node(child.val)
                stack.append(child)
    return d[node]
