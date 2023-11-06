# find longest increasing subsequence
# then find lnogest decreasing subsequence
# find where they intersect 

from bisect import bisect


# Still unsolved; 

def path_lis(nums):
    sub, subindex, trace = [], [], [-1]*(len(nums))
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
    path_index = []
    t = subindex[-1]
    while t >=0: 
        path.append(nums[t])
        path_index.append(t)
        t = trace[t]
    return [path_index[::-1], path[::-1]]       ## index, path

# nums = [1,0,5,4,3,7,2,1,0]
nums = [2,1,4,7,3,2,5]
# neg_nums = [-x for x in nums]

# print(path_lis(nums))
# print(path_lis(neg_nums))

def longestMountain(arr):
    lis = path_lis(arr)
    lds = path_lis([-x for x in arr])
    lds[1] = [-x for x in lds[1]]
    print(lis[0], lds[0])
    cur_max = 0
    for i in range(len(lis[0])-1, -1, -1):
        j = 0
        while lds[0][j] <= lis[0][i]: 
            j +=1
        cur_max = max(cur_max, len(lds[0][j:]) + len(lis[0][:i+1]))

    
    return cur_max

print(longestMountain(nums))

