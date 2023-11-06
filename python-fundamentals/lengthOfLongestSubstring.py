# lengthOfLongestSubstring

def lengthOfLongestSubstring(s):
    uniqueSet = set([char for char in s])
    lenUniques = len(uniqueSet)
    if len(s) == lenUniques:
        return len(s)
    for x in range(lenUniques,1, -1):
        for y in range(len(s) - x+1):
            temp = s[y:y+x]
            unique_temp = set([char for char in temp])
            if len(unique_temp) == x:
                return x
    return 1


# def lengthOfLongestSubstring(s):
#     uniqueSet = set([char for char in s])
#     lenUniques = len(uniqueSet)
#     if len(s) == lenUniques:
#         return len(s)

#     letter_container = {}
#     counter = 0
#     for char in s: 
#         if char in letter_container:
#             letter_container[char] 

#             if counter <= letter_container[char]:
#                 counter 


#     return 1





# s = "ababc"
# s = 'au'
# s = ''
# s = 'a'
s = 'aaasupercsalif'
# length = 8
# uniques = 3

print(lengthOfLongestSubstring(s))


