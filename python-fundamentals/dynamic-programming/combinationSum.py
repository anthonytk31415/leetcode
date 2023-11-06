# 1004
# 15 min 

# combinationSum
# Time: O(n^2) rather, its n *m for n range and m targets
# Space: O(n) for range of targets

def combinationSum(candidates, target):

    cache = {0: [[]]}      ## accepts values from 0 > target

    def helper(candidates, target, cache):
        if target in cache: 
            return cache[target]
        else: 
            res = []
            for c in candidates:
                if target - c >=0: 
                    complement = helper(candidates, target - c, cache)
                    for comp in complement:
                        combo = [c] + comp
                        combo.sort() 
                        res.append(combo)

            res2 = []
            for w in res: 
                if w not in res2: 
                    res2.append(w)
            cache[target] = res2
            return cache[target]
    
    return helper(candidates, target, cache)

print(combinationSum([7,8,6], 17))

### write this out
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:                                  # O(N): for each candidate
            for i in range(c, target+1):                      # O(M): for each possible value <= target
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]
