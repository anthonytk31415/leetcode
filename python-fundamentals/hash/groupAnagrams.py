# groupAnagrams
# hash tables

# def groupAnagrams(strs):
#     container = {}      # key = index, value = {anagram, words}
#     key = 0             # used for making anagramlookup 
#     for s in strs:
#     # build the letter dict
#         anagram = {}
#         for letter in s:
#             if letter not in anagram:
#                 anagram[letter] = 1
#             else: 
#                 anagram[letter] +=1
#         # test if that key exists; if it does, append the word to the key value pair, 
#         completed_loop = False
#         for x in container:
#             if container[x]['anagram'] == anagram:
#                 container[x]['words'].append(s)
#                 completed_loop = True
#                 break
#         # if not, create the key, insert a [word, ]
#         if not completed_loop:
#             container[key] = {'anagram':anagram, 'words':[s]}
#             key +=1
#     return [value['words'] for value in container.values()]


## 90% fast implementation; 
## (n strings ) * (m log m where m = length of str)

# # Intuition
# Variations of anagrams will have the same word in alphabetized order (i.e. 'eat' --> 'aet'; 'tea' --> 'aet').

# We'll make a dictionary 'pairs' with key = alphabetized word, and values = list(actual words). 

# We'll return a list of all the actual words for each key. 

# # Complexity
# - Time complexity:
# O(n=num strings in strs) * (m log m where m = length of str)


def groupAnagrams(strs):          
    pairs = {}
    for x in strs:
        alpha = ''.join(sorted(x))      #m log m for m = len(s)
        if alpha in pairs:
            pairs[alpha].append(x)      # max n for worst-case: n unique, non-anagram strings
        else:
            pairs[alpha] = [x]          
    # return [val for val in pairs.values()] #go over list again, max n unique non-anagram strings
    return list(pairs.values())




# x = 'eat'
# sor = sorted(x)
# sor2 = ''.join(sor)
# print(sor2)



## the official one:
# def groupAnagrams(strs):
#     ans = collections.defaultdict(list)
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         ans[tuple(count)].append(s)
#     return ans.values()



strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))