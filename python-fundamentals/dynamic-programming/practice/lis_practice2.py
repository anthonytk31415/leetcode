from bisect import bisect

def path_lis1(nums):
    sub, subindex, trace = [], [], [-1]*len(nums)
    for i, x in enumerate(nums):
        if len(sub) == 0 or x > sub[-1]:
            if subindex:
                trace[i] = subindex[-1]
            sub.append(x)
            subindex.append(i)
        else:
            idx = bisect(sub, x)
            if idx > 0: 
                trace[i] = subindex[idx-1]
            sub[idx] = x
            subindex[idx] = i
    path = []
    t = subindex[-1]
    while t >= 0: 
        path.append(nums[t])
        t = trace[t]
    return path[::-1]

def path_lis(nums):
    sub, subindex, trace = [], [], [-1]*len(nums)
    for i, x in enumerate(nums):
        if len(sub) == 0 or x > sub[-1]:
            if subindex: 
                trace[i] = subindex[-1]
            sub.append(x)
            subindex.append(i)
        else: 
            idx = bisect(sub, x)
            if idx > 0: 
                trace[i] = subindex[idx - 1]
            sub[idx] = x
            subindex[idx] = i
    path = []
    t = subindex[-1]
    while t >= 0: 
        path.append(nums[t])
        t = trace[t]
    return path[::-1]

nums = [5,3,1,9,6,12, 13, 11]
print(path_lis(nums))

