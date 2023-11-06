# Richard Problem: 1/26/2023


# 7:22

# Time n = len of string; m lenght of wordDict, avg length k
# n^m

# key = substr; val = T/F whether it's in worddict
# c, 0
# ca, 0
# cat, 1


def wordBreak(s, wordDict):
    res = []
    lookup = {}
    for x in wordDict: 
        for i in range(len(x)):
            if i < len(x) - 1:
                if x[0:i+1] not in lookup: 
                    lookup[x[0:i+1]] = 0
            else: 
                lookup[x[0:i+1]] = 1

    print(lookup)
    def helper(substr, lookup, path, res):
        # base case
        if len(substr) == 0: 
            print(path)
            path = " ".join(path)
            res.append(path)
            return 
        # iterative case

        for i in range(len(substr)):
            sub = substr[0:i+1]
            if sub in lookup: 
                if lookup[sub] ==1: 
                    # call recursively 
                    helper(substr[i+1:], lookup, path + [sub], res) 
            else: 
                return

    helper(s, lookup, [], res)
    return res


s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]

print(wordBreak(s, wordDict))