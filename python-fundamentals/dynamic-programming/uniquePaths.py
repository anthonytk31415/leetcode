## this is too slow 


# this stores the permutations; will write another that just stores the length
def uniquePaths(m, n):
    ## (d,r) means d = # of d, r = # r
    ## note that for an m x n board, d = m - 1 total rows, r = n - 1 total columns
    memo = {}
    ## ensure all memos are set in for all d from 1 -> total_d, all r from 1 -> n-1

    # for i or j = 0, the length of the memo is 1 (e.g. 'dddddd', 'rrrr') possible path
    i = 0
    for j in range(0,n):
        memo[(i,j)] = 1

    j = 0
    for i in range(1,m):
        memo[(i,j)] = 1

    ## once you build the "zeroes", you can sequentiall build up the memos up until you get your desired memo
    ## note
    for i in range(1,m):
        for j in range(1,n):
            # d + i - 1, j; # r + i, j - 1
            # memo[(i,j)] = set(['d' + x for x in memo[(i-1, j)]] + ['r' + x for x in memo[(i, j-1)]])
            memo[(i,j)] = memo[(i-1, j)] + memo[(i, j-1)]
    return (memo[(m-1,n-1)])


# a really clean and easy way to understand: 
# look at each pathway from bottom up. 1s when row = 0 or col = 0. 
# then for each subsequent cell, your path is # of total paths coming up and coming left

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]
     

# print(uniquePaths(3,7))
print(uniquePaths(23,12))



    # for i in range(1,m):
    #     for j in range(1,n):
    #         # d + i - 1, j; # r + i, j - 1
    #         newSet = set()
    #         for x in memo[(i-1, j)]:
    #             str = 'd' + x
    #             newSet.add(str)
    #         for x in memo[(i, j-1)]:
    #             str = 'r' + x
    #             newSet.add(str)
    #         memo[(i,j)] = newSet



# permutations
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         ## (d,r) means d = # of d, r = # r
#         ## note that for an m x n board, d = m - 1 total rows, r = n - 1 total columns
#         memo = {}
#         ## ensure all memos are set in for all d from 1 -> total_d, all r from 1 -> n-1

#         i = 0
#         for j in range(0,n):
#             str = 'd'*i + 'r'*j
#             memo[(i,j)] = set([str])

#         j = 0
#         for i in range(1,m):
#             str = 'd'*i + 'r'*j
#             memo[(i,j)] = set([str])

#         for i in range(1,m):
#             for j in range(1,n):
#                 # d + i - 1, j; # r + i, j - 1
#                 memo[(i,j)] = set(['d' + x for x in memo[(i-1, j)]] + ['r' + x for x in memo[(i, j-1)]])