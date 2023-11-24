from collections import Counter, defaultdict



def balancedString(s):
    def checkReqs():
        for char in reqs: 
            if reqs[char] > curCount[char]:
                return False
        return True

    n = len(s)// 4
    charCount = Counter(s)
    reqs = {}
    for char in ["Q", "W", "E", "R"]:
        if charCount[char] > n: 
            reqs[char] = charCount[char] - n
    if not reqs: 
        return 0

    left = 0
    minLength = len(s)    
    curCount = defaultdict(int)
    for right, rightChar in enumerate(s): 
        curCount[rightChar] += 1

        while checkReqs(): 
            minLength = min(minLength, right - left + 1)    
            curCount[s[left]] -= 1
            left += 1
    return minLength

s = "QWER"

# s = "QREQRQWQ"
# s = "QQQW"
# s = "QQWE"

print(balancedString(s)) 