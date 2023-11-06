
# a bfs solution; 

def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)
    visited[0]= True
    q = []
    q.append(0)
    while q:
        u = q.pop()
        for v in rooms[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
    if all(visited): return True
    else: 
        return False

# rooms = [[1,3],[3,0,1],[2],[0]]
# rooms = [[1],[2],[3],[]]
print(canVisitAllRooms(rooms))