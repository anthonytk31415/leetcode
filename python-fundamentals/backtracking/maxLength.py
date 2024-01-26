



def maxLength(arr):
    overallMax = [0]
    curMax = [0]
    chars = [set()]

    def dfs(i):
        if i == len(arr): 
            overallMax[0] = max(overallMax[0], len(chars[0]))
            return 
        elif overallMax[0] == 26: return 
        else: 
            curSet = set(arr[i])
            if len(curSet) == len(arr[i]) and len(curSet.intersection(chars[0])) == 0: 
                chars[0] = chars[0].union(curSet)
                dfs(i+1)
                chars[0] = chars[0] - curSet
            dfs(i+1)            

    dfs(0)
    return overallMax[0]



# arr = ["un","iq","ue"]
arr = ["cha","r","act","ers"]
print(maxLength(arr))

# a = "abc"
# b = "abd"
# a = set(a)
# b = set(b)
# c = a.intersection(b)
# print(c)


# d = "abd"
# d = set(d)
# e = "feg"
# e = set(e)
# f = d.union(e)
# print("f:" , f)
# g = f - e
# print("g:", g)