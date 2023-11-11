# Time: O(m*n) for m items in dictionary, n length of s or length of largest word in dictionary
# Space: O(1)

# just gotta go one by one to see if there's a full match of the word in the dictionary with the s

def findLongestWord(s, dictionary):
    longestWordLength = 0 
    longestWord = ""
    for word in dictionary: 
        i = 0
        j = 0
        while i < len(s):
            if s[i] == word[j]:
                j += 1
            if j >= len(word):
                if len(word) > longestWordLength: 
                    longestWordLength = max(longestWordLength, len(word))
                    longestWord = word
                elif len(word) == longestWordLength:
                    longestWord = min(longestWord, word)                
                break
            i += 1
        
    # if you make i to the end, then you broke above i.e. you found a word match, or 
    # you ran out of chars in your s and thus you didnt find a match
    return longestWord

# print(min("a", ""))

s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]

s = "abpcplea"
dictionary = ["a","b","c"]
print(findLongestWord(s, dictionary))