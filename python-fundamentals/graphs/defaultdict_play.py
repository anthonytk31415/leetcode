from collections import defaultdict

graph = defaultdict(set)

edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]

for u,v in edges: 
    graph[u].add(v)
    graph[v].add(u)

print(graph)

a = set([1,2])
for x in graph:
    temp = set(list(x))
    


print(graph)