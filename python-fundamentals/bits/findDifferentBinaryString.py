from itertools import combinations

def findDifferentBinaryString(nums):
    n = len(nums)
    combos = {0: [""]}
    for i in range(1, n+1):
        print(i, i-1)
        prevBinary = combos[i-1]
        newBinary = []
        for binary in prevBinary: 
            for x in ["0", "1"]:
                newBinary.append(binary + x)

        combos[i] = set(newBinary)
    
    nums = set(nums)
    for x in combos[n]:
        if x not in nums: 
            return x


nums = ["111","011","001"]
print(findDifferentBinaryString(nums))