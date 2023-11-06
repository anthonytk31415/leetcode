# knights moves 

# given i, j, n, return array of valid moves on an n board with prob
# each valid move = [i,j,p] for p = prob 
def knight_move(i,j,n): 
    res = []
    for u,v in [(1,2), (-1,2), (-1,-2), (1,-2), (2,1), (-2,1), (-2,-1), (2,-1)]:
        if 0 <= i+u < n and 0 <= j + v < n: 
            res.append([i + u, j + v])
    return res

def knightProbability(n, k, row, column): 
    res = [[row, column,1.0]] # [row, col, prob]    
    memo = {}
    divisor = 1
    for _ in range(k):
        divisor *= 8
        res_new = []
        for i,j,prob in res: 
            # for each element in res, return the next moves
            if (i,j) not in memo:
                memo[(i,j)] = knight_move(i,j,n)
            possible_moves = memo[(i,j)]         # define psosible moves, then apply the prob

            possible_moves = [x + [prob/divisor] for x in possible_moves]

            res_new = res_new + possible_moves

        res = res_new
    return sum([x[2] for x in res])



    # res = [[row, column,1.0]] # [row, col, prob]    
    # memo = {}
    # for _ in range(k):
    #     res_new = []
    #     for i,j,prob in res: 
    #         print(i,j)
    #         if (i,j) not in memo: 
    #             memo[(i,j)] = knight_move(i,j,n)

    #         possible_moves = memo[(i,j)]
    #         print(possible_moves)
    #         for x in possible_moves:
    #             x.append(prob/8)
    #         res_new = res_new + possible_moves
    #     res = res_new
    #     print(res)



# 2/8 valid moves
# 1,2 
# 2,1
# from here, 2/8 for each 

# 1/4*2/8 + 1/4*2/8

print(knightProbability(3,2,0,0))
# print(knightProbability(4,2,0,0))
# print(knightProbability(1,0,0,0))
    # [[1,2] ,[3,4]] + [[1,4]]