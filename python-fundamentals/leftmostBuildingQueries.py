def leftmostBuildingQueries(heights, queries): 
    res = []
    for a, b in queries: 
        if a > b: 
            a, b = b, a
        # go to j where b is at


        if heights[a] < heights[b]:
            res.append(b)
        elif a == b: 
            res.append(b)
        else:         
            maxHeight = max(heights[a], heights[b])
            maxIdx = max(a, b)

            iStar = maxIdx + 1
            found = False
            while iStar < len(heights):
                if heights[iStar] > maxHeight: 
                    found = True
                    break
                iStar += 1

            if not found: 
                res.append(-1)
            else: 
                res.append(iStar)
    return res

# heights = [6,4,8,5,2,7]
# queries = [[0,1],[0,3],[2,4],[3,4],[2,2]] 

heights = [1,2,1,2,1,2]
queries = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]


x = leftmostBuildingQueries(heights, queries)
print(x, len(x))
# y = [0,1,3,3,5,5,1,1,-1,-1,-1,-1,3,-1,2,3,5,5,3,-1,3,3,-1,-1,5,-1,5,-1,4,5,5,-1,5,-1,5,5]
# z = [0,1,2,3,4,5,1,1,-1, 3,-1, 5,2,-1,2,3,4,5,3, 3,3,3,-1, 5,4,-1,4,-1,4,5,5, 5,5, 5,5,5]

# print(len(y))