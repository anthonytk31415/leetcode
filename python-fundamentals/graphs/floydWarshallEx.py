def floydWarshall(graph):
    # assume graph adjacency list
    vertices = [x for x in graph]
    dist = defaultdict(defaultdict)
    for u in vertices: 
        for v in vertices: 
            if u != v: dist[u][v] = inf
    
    for k in vertices: 
        for i in vertices: 
            for j in vertices: 
                if i != j and j != k and i != k: 
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist