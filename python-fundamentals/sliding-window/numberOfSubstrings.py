
# sliding window: 
# - increase right and update counts. 
# - the moment your window condition is satisfied, add to totalSubs (substrings) the current plus the length of excess from (len(s) - 1) to right for the additional strings  you can add
# - then move left += 1 each time to see if the condition is satisfied. 

# Time: O(n); Spce: O(1)

def numberOfSubstrings(s):
    # invariant: 
    left, right = 0, 0
    counts = {"a": 0,  "b": 0, "c": 0}    
    totalSubs = 0
    while right < len(s):
        counts[s[right]] += 1
        # if counts are satisfied, inc left to shrink and minimize valid window
        while counts["a"] > 0 and counts["b"] > 0 and counts["c"] > 0: 
            rightWidth = (len(s)-1) - right + 1
            totalSubs += rightWidth
            counts[s[left]] -=1
            left += 1
        right += 1
    return totalSubs
    



# 3 left,
# 3 right

# left = 

# 0123456 
s = "aaabcaa"
# s = "abcabc"

print(numberOfSubstrings(s))

# abc
# abca
# abcaa

# aabc
# aabca
# aabcaa

# aaabc
# aaabca
# aaabcaa



# 2*2-1






        