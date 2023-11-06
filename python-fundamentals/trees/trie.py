#Trie implementation

# Performance for storing words in a Trie vs binary tree: 
# -- O(m) for m = length of the for the Trie,  vs 
# -- O(log(n)) for n = depth of the tree

# Insert: 


class TrieNode: 
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children: 
                node.children[w] = TrieNode()
            node = node.children[w]
        # you are now pointing at the node that traversed the last letter
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word: 
            if w not in node.children:
                return False
            else: 
                node = node.children[w]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix: 
            if w not in node.children: 
                return False
            else: 
                node = node.children[w]
        return True