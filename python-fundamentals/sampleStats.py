from collections import defaultdict
from math import inf

def sampleStats(count):
    maximum = -inf
    minimum = inf
    summation = 0
    mode_dict = defaultdict(int)

    for x in count: 
        maximum = max(maximum, x)
        minimum = min(minimum,x)
        mode_dict[x] +=1
        summation += x

    ## calc 

    cur_max = -inf 
    mode = ''
    for y in mode_dict: 
        if mode_dict[y] > 

    mean = summation / len(count)

    res = [minimum, maximum, mean, median, mode]

    return res 