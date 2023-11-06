# trick: 
# start at the water and creep inward with DFS
# you'll traverse DFS if (1) height(new) >= height(cur), and (2) it's not in the "set"
# maintain a set of all the elements you traverse; one for pacific, one for atlantic
# at the end, take all the common elements in pac and atl
# 
# Time: O(N) for N nodes
# Space: O(N) for N nodes


def pacificAtlantic(heights):
# start from water, flow into graph; 
# the result is the graph is visited by both waters
    pacific = set()
    atlantic = set()
    for i in range(len(heights)):
        pacific.add((i,0))
        atlantic.add((i,len(heights[0])-1))

    for j in range(len(heights[0])):
        pacific.add((0,j))
        atlantic.add((len(heights)-1, j))

    def dfs(cell, heights, cell_set):
        (a,b) = cell
        for (i,j) in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
            if 0 <= i < len(heights) and 0 <= j < len(heights[0]) and heights[a][b] <= heights[i][j] and (i,j) not in cell_set:
                cell_set.add((i,j))
                dfs((i,j), heights, cell_set)

    # if you're a candidate and you're not in the set, traverse
    atlantic_initiate = set([x for x in atlantic])
    pacific_initiate = set([x for x in pacific])
    for cell in pacific_initiate: 
        dfs(cell, heights, pacific)

    ## pacific
    for cell in atlantic_initiate:
        dfs(cell, heights, atlantic)

    #consolidate all the common items in one 
    res = []
    for x in pacific: 
        if x in atlantic: 
            (a,b) = x
            res.append([a,b])
    return res 




# def pacificAtlantic(heights):
#     status = {}
#     ocean = {} # ocean[(i,j)][0] = pacific, ocean[(i,j)][1] = atlantic
#     parent = {}
#     all_cells = set()
#     for i in range(len(heights)):
#         for j in range(len(heights[0])):
#             status[(i,j)] = 'undiscovered'
#             ocean[(i,j)] = [False, False]
#             all_cells.add((i,j))

#     def helper(cell, heights, status, ocean):
#         print(cell)
#         status[cell] = 'discovered'
#         (a,b) = cell
#         for (i,j) in [(a+1,b), (a-1,b), (a,b+1), (a,b-1)]:
#         ## test for bordering oceans
#             if i < 0: ocean[(a,b)][0] = True
#             if j < 0: ocean[(a,b)][0] = True
#             if i >= len(heights): ocean[(a,b)][1] = True
#             if j >= len(heights[0]): ocean[(a,b)][1] = True
#         # test for recursive calls
#             if( 0 <= i < len(heights) and 0 <= j < len(heights[0]) 
#                 and heights[a][b] >= heights[i][j]):
#                     if status[(i,j)] == 'undiscovered':
#                         parent[(i,j)] = (a,b)
#                         helper((i,j), heights, status, ocean)
#                 ## inherit pacific/atlantic from descendents
#                     ocean[(a,b)][0] = ocean[(a,b)][0] or ocean[(i,j)][0]
#                     ocean[(a,b)][1] = ocean[(a,b)][1] or ocean[(i,j)][1]

#     for i in range(len(heights)):
#         for j in range(len(heights[0])): 
#             cell = (i,j)
#             if status[cell] == 'undiscovered':
#                 helper(cell, heights, status, ocean)
#     res = []
#     for x in ocean: 
#         (a,b) = x
#         if ocean[(a,b)][0] and ocean[(a,b)][1]:
#             res.append([a,b])
#     print(parent)
#     return res

# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
h = [[3,3,3],[3,1,3],[0,2,4]]
z = pacificAtlantic(h)
print(z)
