from collections import defaultdict
# Time: O(n)
# Space: O(n)

def findAndReplacePattern(words, pattern):

    def word_to_code(word):
        counter = 0
        code_converter = {}
        code = ''
        for i in range(len(word)):
            if word[i] not in code_converter: 
                code_converter[word[i]] = counter
                counter +=1
            code = code + '-' + str(code_converter[word[i]])
        return code

    lookup = set()
    lookup.add(word_to_code(pattern))
    res = []
    for word in words: 
        code = word_to_code(word)
        if code in lookup: 
            res.append(word)
    return res

# words = ["abc","deq","mee","aqq","dkd","ccc"]
# pattern = "abb"

words = ["abcdefghijkba"]
pattern = "qwertyuiopwqa"

print(findAndReplacePattern(words, pattern))