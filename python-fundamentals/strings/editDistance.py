# find the largest common in order substring 
## this allows you to save replace/remove/adds 

# 
# replace letters
# remove or add new ones

def minDistance(word1, word2):
    len1, len2 = len(word1), len(word2)
    substr = ''
    i = j = 0
    while i < len1 and j < len2: 
        if word1[i] == word2[j]:
            substr += word1[i]
            i +=1
            j +=1


# daaabbc 
# dbca


# abcd 

# intention
# ExecuTION



# ETION 
# exEcuTION

# horse
# ro*s*
# x_*_*

# 3 moves: 
# remove only; then overlaps 

# in both cases: 
# transform is capped by len1: max transform len1 times


# if len1 >= len2: then transform, remove 
# - remove is fixed at (len1 - len2) times. 
# - 


# if len1 < len2: then transform, add
# - add is fixed at (len2 - len1) times.

# Ex1: 
# aaa
# bbbbb

# transform: aaa -> bbb
# then add: bb

# Ex2: 
# baa**
# bbbbb

# transform 2 times: aa -> bb
# then add bb

# *aaa*
# baaab
# add b front and back; 2 adds that's it

# Ex: 
# *aacp
# baaab
#  aacp
# -- what element to shift w1 so that you get maximal matches by index?
# -- then teh rest transform

# baaab
#  aca
