from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = [None]*256
        self.word = None

    def insert(self, word, trie, cur_path):
        if not word: 
            trie.word = cur_path
            return 
        else:
            if trie.children[ord(word[0])]:
                new_trie = trie.children[ord(word[0])]
            else:                 
                new_trie = Trie()
                trie.children[ord(word[0])] = new_trie
            self.insert(word[1:], new_trie, cur_path + word[0])
    
    def traversal(self, trie):
        res = []
        if not trie: 
            return res
        
        if trie.word: res.append(trie.word)

        for x in range(len(trie.children)): 
            if trie.children[x]: 
                res = res + self.traversal(trie.children[x])
        return res


from math import inf 
# traverse only if there's an existing word there

def longestWord(words):
    root = Trie()
    for word in words: 
        root.insert(word, root, '')

    res = [-inf, None]          ## length, word

    def dfs(root, res):
        for i in range(len(root.children)):
            if root.children[i] and root.children[i].word:
                if len(root.children[i].word) > res[0]:
                    res[0] = len(root.children[i].word)
                    res[1] = root.children[i].word
                elif len(root.children[i].word) == res[0]:
                    res[1] = min(res[1], root.children[i].word)
                dfs(root.children[i], res)
    dfs(root, res)

    return res[1]


# words = ["w","wo","wor","worl","world"]
# words = ["a","banana","app","appl","ap","apply","apple"]
words = ["wo","wor","worl","world"]

z = longestWord(words)
# print(z.children[ord('w')].children[ord('o')].word)
print(z)