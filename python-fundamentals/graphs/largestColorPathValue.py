# that was a fucking hard topological sort

# do topological sort: 
# to do this, formulate a graph with adjacency list
# then create nodegrees array for each node and for each edge, if the arrival node (v) exists, +=1 (you're counting parents)
# then create a queue of nodegree = 0 nodes. 
# create a topological sort array; when they dependencies are 0 i.e. you've either popped them previoiusly or they started as 0
# the loop: while queue: 
# pop a node, and then everytime you pop, you append the node to the topo sort array
# then for each v in the child/graph array: 
# specific to this problem, you'll want to include a colorCounter[v] for each v that will include the max count of each letter
#       note that a node v can have multiple parents, but you're only interested in the max count for each letter (so you dont have to store a tree, just the  max count)
#       carry that max count over to v and update
#       reduce the nodegrees[v] -=1 and if nodegrees[v] == 0: add it to the queue

# you do this until you have no more vertices with 0 

# if at the end you have no cycles, then the length of the topo sort is equal to the number of nodes; 
#   if so, iterate through the colorCounter[v]'s and get the max count for each and return the max count of a color

# if not, you'll have a cycle and you return -1

from collections import defaultdict, Counter, OrderedDict

from math import inf

class colorCount:
    def __init__(self):
        self.color = {}
        for x in 'abcdefghijklmnopqrstuvwxyz':
            self.color[x] = 0

def largestPathValue(colors, edges):

    graph = defaultdict(list)
    n = len(colors)
    # do topological sort

    indegrees = {node: 0 for node in range(n)}
    colorCounter = {node: colorCount() for node in range(n)}
    for u, v in edges: 
        indegrees[v] +=1
        graph[u].append(v)

    nodes_with_no_incoming_edges = []
    for node in range(n):
        if indegrees[node] == 0:
            nodes_with_no_incoming_edges.append(node)

    topological_ordering = []

    while nodes_with_no_incoming_edges:
        u = nodes_with_no_incoming_edges.pop()
        colorCounter[u].color[colors[u]] +=1
        topological_ordering.append(u)
        for v in graph[u]:
            indegrees[v] -= 1 
            v_colors = colorCounter[v].color
            u_colors = colorCounter[u].color
            for c in v_colors:
                v_colors[c] = max(v_colors[c], u_colors[c])
            if indegrees[v] == 0: 
                nodes_with_no_incoming_edges.append(v)

    if len(topological_ordering) == n:
        # print('success')
        res = -inf
        for x in colorCounter:
            res = max(res, max(list(colorCounter[x].color.values())))
        return res
    else: 
        return -1

    # each node will have a counter for a, b, c, .... z where it'l store the max count 
    # we'll start with the noegrees, we'll count the parents for each node



colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]

# colors = "hhqhuqhqff"
# edges = [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]

# edges = [[0,2],[3,0],[1,3],[4,1]]
# colors = "bbbhb"
# colors = "a"
# edges = [[0,0]]
print(largestPathValue(colors, edges))
