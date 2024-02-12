def isAdditiveNumber(num):
    tracker = []

    # returns an array of  strings
    def buildCandidate(i):
        candidates = []
        if len(tracker) < 3: 
            for j in range(len(num)//(3 - len(tracker)) + 1):
                candidate = num[i:i+j+1]
                candidates.append(candidate)

        else: 
            prevLen = len(tracker[-1])
            candidates.append(num[i:i+prevLen])
            if i + prevLen < len(num): candidates.append(num[i:i+prevLen + 1])
        return candidates


    # i is teh current index where you havent chosen nums yet
    def dfs(i):
        if i == len(num):
            if len(tracker) >= 3: return True
            else: return False

        candidates = buildCandidate(i)
        # print(candidates)
        for x in candidates: 
            if x[0] == "0" and len(x) >1: break
            idx = i + len(x)
            # print("next cand: ", x, tracker)
            # if len(tracker) >= 2: print("sum 1 and 2: ", )
            if len(tracker) < 2 or int(tracker[-1]) + int(tracker[-2]) == int(x):
                tracker.append(x)
                if dfs(idx): return True
                tracker.pop()
        return False

    return dfs(0)

# num = "112358"
# num = "199100199"
# num = "1023"
# num = "111"
# num = "112"
# num = "113"
# num = "101"
num = "121474836472147483648"
print(isAdditiveNumber(num))