


def wordBreak(s, wordDict):
    memo = {'': True}

    def helper(s, wordDict, memo):
        if s in memo: 
            return memo[s]
        res = []
        for x in wordDict: 
            if x == s[:len(x)]:
                res.append(helper(s[len(x):], wordDict, memo))
        res = any(res)
        memo[s] = res
        return res

    return helper(s, wordDict, memo)

# s = "leetcode"
# wordDict = ["leet","code"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

print(wordBreak(s, wordDict))