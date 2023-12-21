from collections import deque, defaultdict

# Trie Implementation
# Time: O(m*n) for m words in sentence, n max letters in word
# Space: O(m*n*k) for the trie, m words, n letters, k total chars 

def replaceWords(dictionary, sentence):

    class Trie: 
        def __init__(self, val=None): 
            self.val = val 
            self.word = False
            self.children = defaultdict(Trie)

    # store words as an array
    def insertWord(trie, word):
        def insertWordHelper(trie, wordDeque): 
            if not wordDeque: 
                trie.word = True
                return 
            char = wordDeque.popleft()
            insertWordHelper(trie.children[char], wordDeque)
        
        return insertWordHelper(trie, deque([x for x in word]))

    def isWordInTrie(trie, word):
        def isWordInTrieHelper(trie, wordDeque, wordArrSoFar):
            if trie.word == True: return ''.join(wordArrSoFar)
            if not wordDeque: return False
            curLetter = wordDeque.popleft()
            if curLetter not in trie.children: return False
            wordArrSoFar.append(curLetter)
            return isWordInTrieHelper(trie.children[curLetter], wordDeque, wordArrSoFar)
        return isWordInTrieHelper(trie, deque([x for x in word]), [])

    trie = Trie()
    for word in dictionary: 
        insertWord(trie, word)

    res = []
    for word in sentence.split(' '): 
        newWord = isWordInTrie(trie, word)
        if newWord == False: res.append(word)        
        else: res.append(newWord)

    return ' '.join(res)

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"


# dictionary = ["a","b","c"]
# sentence = "aadsfasf absbs bbab cadsfafs"

print(replaceWords(dictionary, sentence))





# t = Trie()
# wordDeque = deque([x for x in "taylor"])
# insertWord(t, wordDeque)
# wordDeque = deque([x for x in "tatum"])
# insertWord(t, wordDeque)


# print(t.children["t"].children["a"].children["y"].children["l"].children["o"].children["r"].word)
# print(t.children["t"].children["a"].children["t"].children["u"].children["m"].word)

# print(''.join(["a", "b", "c"]))

# wordDeque = deque([x for x in "blah"])
# print(isWordInTrie(t, wordDeque, []))

