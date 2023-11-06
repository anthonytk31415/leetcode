# lis_practice

from bisect import bisect, bisect_left, bisect_right

# the length 

def lis(nums):
    subs = [nums[0]]
    if len(nums) <= 1: 
        return len(subs)
    for i in range(1 ,len(nums)):
        print(subs, nums[i])
        if nums[i] > subs[-1]:
            subs.append(nums[i])
        else: 
            idx = bisect(subs, nums[i])
            subs[idx] = nums[i]
    return len(subs)



# print(lis(nums))


## return 

def path_lis3(nums):
    sub = []
    subIndex = []                           # store the index of nums where subs is 
    trace = [-1]*len(nums)                  # trace[i] points to the index of previous in LIS
    for i, x in enumerate(nums):
        print(x, 'trace:', trace, 'subindex: ', subIndex, 'sub:', sub)
        if len(sub) == 0 or x > sub[-1]:    # for the first element, add
            if subIndex:                    # need a previous ot initiate
                trace[i] = subIndex[-1]
            sub.append(x)
            subIndex.append(i)
        else: 
            idx = bisect(sub, x)
            print('idx', idx)
            if idx > 0: 
                trace[i] = subIndex[idx-1]
            sub[idx] = x
            subIndex[idx] = i
    print('trace:', trace, 'subindex: ', subIndex, 'sub:', sub)
    path = []
    t = subIndex[-1]
    while t >= 0: 
        path.append(nums[t])
        t = trace[t]
    return path[::-1]



def path_lis2(nums):
    sub = []
    subindex = []                           # wherever you insert x with sub, trace will pick up the last subindex in LIS
    trace = [-1] * len(nums)                # keeps track of the previous LIS element index form nums
    for i, x in enumerate(nums):
        if len(sub) == 0 or x > sub[-1]:    # x is the largest element found
            if subindex:
                trace[i] = subindex[-1]     # map trace to the previous LIS
            sub.append(x)
            subindex.append(i)
        else: 
            idx = bisect(sub, x)
            if idx > 0:                     # note if idx = 0, there is no previous LIS
                trace[i] = subindex[idx-1]  # map trace to the previous LIS
            sub[idx] = x
            subindex[idx] = i
    path = []                               # build the path
    t = subindex[-1]                        # start from the largest and work to the smallest
    while t >= 0:
        path.append(nums[t])
        t = trace[t]
    return path[::-1]                       # return reversed path
    

def path_lis3(s):
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


def path_lis4(nums):
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

def path_lis5(nums):
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


def path_lis6(nums):
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
    while t >=0: 
        path.append(nums[t])
        t = trace[t]
    return path[::-1]

def path_lis7(nums):
    sub, subindex, trace = [], [], [-1]*len(nums)
    for i, x in enumerate(nums):
        if len(sub) == 0 or x > sub[-1]:
            if subindex:
                trace[i] = subindex[-1]
            sub.append(x)
            subindex.append(i)
        else: 
            idx = bisect(sub, x)
            if idx >0: 
                trace[i] = subindex[idx - 1]
            sub[idx] = x
            subindex[idx] = i
    path = []
    t = subindex[-1]
    while t >= 0: 
        path.append(nums[t])
        t = trace[t]
    return path[::-1]


# for non-decreasing, x needs to be >= sub[-1]. 
# We always update duplicate entries (use bisect) on the right

def path_lis(nums):
    sub, subindex, trace = [], [], [-1]*len(nums)
    for i, x in enumerate(nums):
        print(sub, x)
        if len(sub)== 0 or x >= sub[-1]:
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
    while t >=0: 
        path.append(nums[t])
        t = trace[t]
    return path[::-1]


def path_lis(nums):
    sub, subindex, trace = [], [], [-1]*len(nums)
    for i, x in enumerate(nums):
        if len(sub) == 0 or x >= sub[-1]:
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

nums = [10, 15, 11, 13, 6, 4, 13, 20, 21, 18, 8, 33, 13, 44, 10, 14, 15, 16, 18]
# nums = [10, 15, 11, 13, 6]
print(path_lis(nums))