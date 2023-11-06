# findCenter
# https://leetcode.com/problems/find-center-of-star-graph/




def findCenter(edges):
    if edges[0][0] in edges[1] and edges[0][0] in edges[2]:
        return edges[0][0]
    
    else: 
        return edges[0][1]