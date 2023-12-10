def getGoodIndices(variables, target):
    res = []
    for i, variable in enumerate(variables): 
        a = variable[0] 
        b = variable[1] 
        c = variable[2] 
        m = variable[3] 
        
        if (((a**b) % 10)** c ) % m == target: 
            res.append(i)
    return res

# variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]]
# target = 2

variables = [[39,3,1000,1000]]
target = 17
print(getGoodIndices(variables, target))