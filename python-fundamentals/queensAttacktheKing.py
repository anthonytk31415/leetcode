from collections import defaultdict




# def buildDirs(direction, x, y, xPlus, yPlus):
#     x += xPlus
#     y += yPlus
#     while 0 <= x <= 7 and 0 <= y <= y: 
#         dirs[direction].append((x, y))
#         x += xPlus
#         y += yPlus


def queensAttacktheKing(queens, king):
    def distance(x0, y0, x1, y1):
        return ((x0 - x1)**2 + (y0 - y1)**2)**(1/2)

    def buildDirs(direction, x, y, xPlus, yPlus):
        x += xPlus
        y += yPlus
        while 0 <= x <= 7 and 0 <= y <= 7: 
            dirs[direction].add((x, y))
            x += xPlus
            y += yPlus

    x, y = king
    dirs = defaultdict(set)
    queenDirs = defaultdict(list)
    x, y = king
    directions = ["SE", "NE", "NW", "SW", "U","L","R","D"]
    dirMoves = [(1,1),(-1,1),(-1,-1),(1,-1),(-1,0),(0,-1),(0,1),(1,0)]

    for direction, dirMove in zip(directions, dirMoves):
        xPlus, yPlus = dirMove
        buildDirs(direction, x, y, xPlus, yPlus)

    for queen in queens: 
        xq, yq = queen 
        for direction in directions: 
            if (xq, yq) in dirs[direction]: 
                queenDirs[direction].append((xq, yq)) 
                break    
    res = []
    for direction in [x for x in queenDirs]: 
        queenDirs[direction].sort(key = lambda w: distance(x,y,w[0],w[1]))
        res.append(queenDirs[direction][0])
    
    return res

queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]

print(queensAttacktheKing(queens, king))