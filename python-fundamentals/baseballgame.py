def calPoints(operations):
    res = []
    for x in operations:
        if x.isnumeric() or (x[0] == '-' and x[1:].isnumeric()):
            res.append(int(x))
        elif x == 'C':
            res.pop()
        elif x == 'D':
            res.append(res[-1]*2)
        elif x == '+':            
            res.append(res[-1] + res[-2])
        print(res)
    return sum(res)


ops = ["5","-2","4","C","D","9","+","+"]

print(calPoints(ops))