# 930; took me 30 min

# Two pointers: one on the left, one on the right
# - each step, increment r
# - keep a count of the chars
# - if there are no repeats (char count for a char <= 1): update the max length
# - if you hit a repeat, increment l until you get to the repeat, then do one more step to get a "clean" non-repeat L-R substring
#       - as you are incrementing L to find the non-repeats, take out the char from the char count 


# Time: O(n) - run through the chars of the string potentially twice
# space: O(n) - to store counts

def lengthOfLongestSubstring(s):
    track={}
    max_length = 0
    l = 0
    for r in range(len(s)):
        if s[r] not in track: 
            track[s[r]] = 0
        track[s[r]] +=1
        # if you dont have a repeating, update max length; 
        # repeating: when the current letter count > 1 
        if track[s[r]] <= 1: 
            cur_max = r - l + 1
            # print(l, r, cur_max)
            if max_length < cur_max:
                max_length = cur_max 
        # if you have a repeating, take the last one out (the left string), increment L +=1
        else: 
            while s[l] != s[r]: 
                track[s[l]] -=1
                l +=1
            track[s[l]] -=1
            l +=1
    return max_length 

print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("aab"))