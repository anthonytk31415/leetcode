from collections import defaultdict, deque

def calcEquation(equations, values, queries): 
    graph = defaultdict(list)
    for i, (u,v) in enumerate(equations): 
        val = values[i]
        graph[u].append((v, val))
        graph[v].append((u, 1/val))

    def bfs(start, end):
        if start not in graph: 
            return -1
        queue = deque([(start, 1, set([start]))])
        res = 1
        while queue: 
            u, u_val, u_visited = queue.popleft()
            if u == end: 
                return u_val
            u_visited = set(list(u_visited) + [u])
            for v, v_val in graph[u]:
                if v not in u_visited: 
                    
                    queue.append((v, u_val * v_val, u_visited))
        return -1
    
    res = []
    for u, v in queries: 
        res.append(bfs(u, v))

    return res

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(calcEquation(equations, values, queries))

# queue = deque(["1", "2"])
# print(queue.popleft())
# print(queue.popleft())
# # print(queue.popleft())

# v_visited = set([1,2]) 
# v_visited = list(v_visited) + [3]
# # print(v_visited)
# # print()