def path_exists(pairs, i, j, pairVisited):

    def peHelper(i, pairs, pairVisited, path):
        if i == j: 
            return path
        pairVisited.add(i)
        for u, v in pairs: 
            if u == i and v not in pairVisited:
                return peHelper(v, pairs, pairVisited, path + [[u, v]])

    return peHelper(i, pairs, pairVisited, []) 


# s = "cba"
# pairs = [[0,1],[1,2]]
# print(path_exists(pairs, 0, 2, set()))


def smallestStringWithSwaps(s, pairs):
    visited = set()
    pairVisited = set()
    arr = [x for x in s]
    min_arr = sorted(arr)
    # i = array index in arr that you want to minimize 
    # j = array index in min_array that you can possibly swap into arr's i to get the smallest array possible
    def dfs(arr, i, j):
        print(arr, i, j)
        # if i >= len(arr) then you are done! return arr
        if i >= len(arr):
            return arr

        # if j >= len(arr): then arr[i] is already largest. add arr[i] into visited, i +=1, 
        # take the next j such that min_arr[j] is smallest and min_arr[j] not in visited, 
        if j >= len(arr):
            visited.add(arr[i])
            return dfs(arr, i+1, 0)            

        if min_arr[j] in visited: 
            return dfs(arr, i, j+1)

        # check if you can do a series of swaps from arr so that arr[i] = min_arr[j]. swaps cannot include anything in visited.
        # if so, do the swap, take the next j such that min_arr[j] is smallest and min_arr[j] not in visited, 
        # add arr[i] into visited (after i got swapped), i +=1, 

        idx = arr.index(min_arr[j])

        path = path_exists(pairs, i, idx, pairVisited)
        print('path', path, i,idx)
        if path: 
            for e in range(len(path)-1, -1, -1):
                x, y = path[e] 
                arr[x], arr[y] = arr[y], arr[x]
                visited.add(arr[i])
            return dfs(arr, i+1, 0)

        # if not, j += 1
        if not path: 
            return dfs(arr, i, j +1)
        
    return ''.join(dfs(arr, 0, 0))

# s = "dcab"
# pairs = [[0,3],[1,2]]
s = "dcab"
pairs = [[0,3],[1,2],[0,2]]


# s = "cba"
# pairs = [[0,1],[1,2]]

# s = "vbjjxgdfnru"
# pairs = [[8,6],[3,4],[5,2],[5,5],[3,5],[7,10],[6,0],[10,0],[7,1],[4,8],[6,2]]

print(smallestStringWithSwaps(s, pairs))

## too slow
    # visited = set()
    # arr = [x for x in s]
    # cur_min = [tuple(arr)]
    
    # def dfs(arr):
    #     visited.add(tuple(arr))
    #     if tuple(arr) < cur_min[0]:
    #         cur_min[0] = tuple(arr)
    #     for i, j in pairs: 
    #         arr_new = [x for x in arr]
    #         arr_new[i], arr_new[j] = arr_new[j], arr_new[i]
    #         if tuple(arr_new) not in visited:
    #             dfs(arr_new)

    # dfs(arr)
    # return ''.join(cur_min[0])