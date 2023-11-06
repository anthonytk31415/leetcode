def hammingDistance(x: int, y: int) -> int:
    if y > x:           # always make x larger than y 
        x, y = y, x
    x = bin(x)[2:]
    y = bin(y)[2:]
    if len(x) > len(y):
        y = '0' * (len(x) - len(y)) + y
    counter = 0
    for i in range(len(x)): 
        if x[i] != y[i]:
            counter +=1
    return counter

print(hammingDistance(1,4))