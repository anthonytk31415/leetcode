
# note you are indexed starting at 1
def generate(numRows): 
    res = [[1]]

    if numRows == 1: 
        return res
    else: 
        for i in range(2, numRows+1):
            between = []
            for n in range(len(res[-1])-1):
                between.append(res[-1][n] + res[-1][n+1])
            res.append([1] + between + [1])
            # print(res)
        return res

print(generate(5))