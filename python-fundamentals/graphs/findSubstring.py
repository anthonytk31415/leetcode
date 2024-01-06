from collections import Counter, defaultdict, deque

# We first build a trie for all words to check linearly. We also associate a unique id for every position in the trie.  
# This is so when we traverse the s, we want to prevent visisting the same trie node twice with each ith position of s. 

# Then, we effectively dfs for each char in s but with a twist: if the first char is a member of the trie, we traverse. 
# Once we find a word in the trie, we reset the trie, and add the word into a deque. We also keep track of number of words in the 
# words and number of word we've found. If we've found more than the number of words of the word type, we popleft from the deque 
# until that number == words in the word check (this is so if we get repeats of the word, we dont have to start over, but start
# at the posiiton of when we have just enough words). When we popleft, we increase our idx by wordlength since our starting point is 
# effectively increased with each popleft. 
# Then we continue. If we find that the deque lenght is equal to the words length
# we append the initial index to our result. 

# We have to DFS each ith position in case the 2nd or 3rd posiitons of a word is the start of another word. 

# Time: O(n*s) for n max length of words, for s length of string; 
# Space: O(MN) for m words, n max length

def findSubstring(s, words):

    class TrieNode: 
        def __init__(self):
            self.isWord = False
            self.children = {}   
            self.id = 0
            
    # Build Trie
    lenWord = len(words[0])
    trie = TrieNode()
    trieId = 1
    for word in words: 
        node = trie
        for w in word: 
            if w not in node.children: 
                node.children[w] = TrieNode()
                node.children[w].id = trieId
                trieId += 1
            node = node.children[w]
        node.isWord = True

    wordCount = Counter(words)
    visited = set()
    res = []
    for j in range(len(s)):
        node = trie
        wordChain = deque()
        curWordCount = Counter()
        curWord = []
        idx = j

        for i in range(j, len(s)):
            char = s[i]
            if char in node.children and (i, node.id) not in visited: 
                visited.add((i, node.id))
                node = node.children[char]
                curWord.append(char)

                # assess word is True
                if node.isWord == True: 
                    fullWord = "".join(curWord)
                    wordChain.append(fullWord)
                    curWordCount[fullWord] += 1
                    # if you have a duplicate word, remove based on order of when you put them in
                    while curWordCount[fullWord] > wordCount[fullWord]:
                        idx += lenWord
                        wordToRemove = wordChain.popleft()
                        curWordCount[wordToRemove] -=1
                    
                    # is this a winning combo? 
                    if len(words) == len(wordChain): res.append(idx)

                    # reset conditions of word
                    node = trie
                    curWord = []
            else: 
                break

    return res


# print(trie.children, trie.children["f"].children, trie.children["f"].children["o"].children)    

s = "barfoothefoobarman"
words = ["foo","bar"]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]


s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]


s = "aaaaaaaaaaaaaa"
words = ["aa", "aa"]
print(findSubstring(s, words))

# print("".join(["a","b"]))