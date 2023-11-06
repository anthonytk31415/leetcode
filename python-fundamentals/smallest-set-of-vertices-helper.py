#smallest set of vertices helper

x = [[0,1],[0,2],[2,5],[3,4],[4,2]]
edges = x

def vertex_to_edges(edges, vertex):
    return list(filter(lambda x: x[1] == vertex, edges))


def vertex_from_edges(edges, vertex):
    return list(filter(lambda x: x[0] == vertex, edges))


to_edges = vertex_to_edges(x, 2)
from_edges = vertex_from_edges(x, 2)
print(to_edges)
print(from_edges)

n = 6
set1 = set([x for x in range(n)])
print(set1)

all_nodes = set([x for x in range(n)])
nodes_with_path_to = set([x[1] for x in edges])         ## get list of vertices with path to (i.e. [1,2] means 2 has a "path to")

nodes_no_path_to = all_nodes - nodes_with_path_to
print(nodes_no_path_to)

nodes_traversed = {}

for node in nodes_no_path_to