


def permutations(lst):
    memo = {}
    def permHelper(lst, memo):
        if tuple(lst) in memo: 
            return memo[tuple(lst)]
        else: 
            if len(lst) == 1: 
                res = [lst]
            else: 
                res = []
                for i in range(len(lst)):
                    x = lst[i]
                    complement = lst[:i] + lst[i+1:]
                    for y in permHelper(complement, memo):
                        z = [x] + y
                        if z not in res: res.append(z) 
            memo[tuple(lst)] = res
            return memo[tuple(lst)]
    return permHelper(lst, memo)

def nextPermutation(nums):
    perms = permutations(sorted(nums))
    index = perms.index(nums)
    if index + 1 == len(perms):
        newNums= perms[0]
    else: 
        newNums= perms[index + 1]
    for i in range(len(nums)):
        nums[i] = newNums[i]


nums = [3,1,4,4,2,3,4,0,0]
# print(permutations(nums))
print(nextPermutation(nums))
print(nums)




# lst = [1,1,3]
# print(permutations(lst))

