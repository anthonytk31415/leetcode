# longestSubstring

# Longest Substring with At Least K Repeating Characters

# from collections import defaultdict

# for trivial cases, if len(s) == 0 or k > len(s) return 0
# concept: 
# build a counter of chars from the Counter import
# - for chars with count < k: you they'll never be part of your solution. 
#   So split them and then call on the function recursively. Take the max of each of their outputs
#   so the largest one wins. 
# - for chars with countChar[c] >=k: skip over until 
# - the terminal condition is when the full string you evaluate contains nothing but chars >= k, and the length
#   of that string will flow to the max current.  
# 
# great use of for-else (with a break)
# Time: 
#  - note that every time you do another loop on the substring, youre calling the function again on a shorter substring w/o that character; so at 
#  - most you'll call the function 26 times on the string. --> O(26N) = O(N)
# Space: 
#  - you'll keep a count of the substrings which will be constant (max 26 strings) = O(1)

from collections import Counter
def longestSubstring(s, k):
    if k > len(s) or len(s) == 0:
        return 0
    countChar = Counter(s)
    curMax = 0
    for c in s: 
        if countChar[c] < k: 
            removed_c = s.split(c)
            curMax = max([longestSubstring(x, k) for x in removed_c])
            break
    else: 
        curMax = max(curMax, len(s))
    return curMax

print(longestSubstring('cdababcdab', 2))


# def longestSubstring(s, k):
#     if k == 1:
#         return len(s)
    
#     lookup = defaultdict(list)
#     res = 0
#     for i in range(len(s)):
#         c = s[i] 
#         lookup[c].append(i)
#         if len(lookup[c]) >= k:
            

# s = 'anthonytrankiem'
# c = 'h'
# print(s.count(c))

# splitted = s.split(c)
# print(splitted)