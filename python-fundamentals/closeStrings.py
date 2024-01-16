from collections import Counter, defaultdict

def closeStrings(word1, word2):
    # char1, char2 = set(), set()
    w1, w2 = Counter(word1), Counter(word2)
    charFreq1, charFreq2 = Counter(), Counter()
    wordCounts = [w1, w2]
    charFreqs = [charFreq1, charFreq2]

    for i in range(len(wordCounts)):
        w = wordCounts[i]
        charFreq = charFreqs[i]
        for char in w:
            charFreq[w[char]]+= 1
    print(set(w1.keys()), set(w2.keys()))

    if w1.keys() != w2.keys(): return False
    for num in charFreq1.keys():
        if num not in charFreq2 or charFreq1[num] != charFreq2[num]: return False

    return True

word1 = "cabbba"
word2 = "abbccc"

# # word1 = "a"
# # word2 = "aa"
# word1 = "abc"
# word2 = "bca"

# word1 = "uau"
# word2 = "ssx"

print(closeStrings(word1, word2))