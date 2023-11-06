# def minExtraChar(s, dictionary):
#     memo = {}

#     def dp(s):
#         if s in memo: 
#             return memo[s]
#         res = len(s)
#         if len(s) != 0: 
#             for word in dictionary: 
#                 i, j = 0, 0     # i for s, j for word
#                 while i < len(s) :
#                     if s[i] == word[j]:
#                         j += 1
#                     else: 
#                         j = 0
#                     i += 1
#                     if j == len(word):
#                         leftString = s[:i - (j - 1)]
#                         rightString = s[i:]
#                         # print(f"i: {i}, j: {j}, ls: {leftString}, rs: {rightString}, word found: {word}, on string: {s}")
#                         curRes = dp(leftString) + dp(rightString)
#                         # print(dp(leftString), dp(rightString))
#                         if curRes < res:
#                             res = curRes
#                         j = 0    
#         memo[s] = res
#         # print(s, res)
#         return res

#     return dp(s)        


# s = "leetscode"
# dictionary = ["leet", "code"]

# s = "leetscode"
# dictionary = ["leet","code","leetcode"]

# s = "sayhelloworld"
# dictionary = ["hello","world"]

# s = "dwmodizxvvbosxxw"
# # #    _xxxxxx_xx_x____    

# dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]


from collections import defaultdict
def minExtraChar(s, dictionary): 
    n = len(s)
    wordDict = defaultdict(list)
    
    for word in dictionary: 
        wordDict[word[0]].append(word)

    res = [0] * (n + 1)
    
    for i in range(n - 1, -1, -1):
        print(i, res[i])
        
        res[i] = res[i + 1] + 1

        if s[i] in wordDict: 
            for word in wordDict[s[i]]:
                if s[i : i + len(word)] == word: 
                     res[i] = min(res[i], res[i + len(word)])

    return res[0]

def minExtraChar2(s, dictionary): 
    # Get the length of the input string 's'
    n = len(s)
    
    # Create a defaultdict 'word_dict' to store words grouped by their first characters
    word_dict = defaultdict(list)
    
    # Populate 'word_dict' with words from the 'dictionary' list
    for word in dictionary:
        word_dict[word[0]].append(word)
        
    # Initialize a list 'result' of length 'n+1' to store minimum extra characters at each position
    result = [0] * (n + 1)
    
    # Iterate through the string 's' from right to left
    for i in range(n - 1, -1, -1):
        # Initialize the current position in 'result' with one more extra character than the next position
        result[i] = result[i + 1] + 1
        
        # Check if the current character 's[i]' is found in 'word_dict'
        if s[i] in word_dict:
            # Iterate through the words that start with 's[i]'
            for word in word_dict[s[i]]:
                # Check if the substring starting at position 'i' matches the current word
                if s[i:i + len(word)] == word:
                    # Update 'result[i]' with the minimum of its current value and 'result[i + len(word)]'
                    result[i] = min(result[i], result[i + len(word)])
                    
    # Return the minimum number of extra characters left when breaking the string optimally
    return result[0]

s = "mrmarmrmar" ## this is 10 length
# s = "smrmardscsgfhzliphzadmrmarwghhzgsmrmarhzh"
# s = "smrmardscsgfhzliphzadmrmarwghhzgsmrmarhzh"
# s mrmar dscsg f hz lip hz ad mrmar wgh hz gs mrmar hz h
 
dictionary = ["mrmar","hz","dscsg"]
# 13


print(minExtraChar(s, dictionary))



# print(s[1:3])