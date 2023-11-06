# - the trick is to build a trie for each of the words
# - then, for each cell on the board, you will make sure that the current cell is in the Trie's child
#     - if so, then traverse the Trie by one by calling it for each next potential node 
#           (i.e. exploring the current node)
#     - you'll do so by a DFS traversal
#     - potential nodes are ones within the board: i>= 0 and i <= len(board) - 1 and j >= 0 and j <= len(board[0])-1 
#     - to ensure you only mark a word once, when you get to the end node where node.word == True, 
#           then mark it False so subsequent traversals do not trigger it
#     - when you recursively call DFS on the next node, you'll mark the current board[i,j] 
#           as # so that if you traverse on it again if it is a potential candidate, 
#           you're guaranteed not have that board[i,j] be in the node's children. 
#           after the DFS recursive call, you'll set the board[i,j] back to it's original content
#     - 



class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word: 
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.word = True

    # def search(self, word):
    #     node = self.root
    #     for w in word: 
    #         if w not in node.children:
    #             return False
    #         else: 
    #             node = node.children[w]
    #     return node.word == True

class Solution:
    def findWords(self, board, words):
        def dfs(board, i, j, node, path):
            if node.word: 
                res.append(path)
                node.word = False
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return 
            w = board[i][j]
            if w not in node.children:
                return 
            ## test boundary conditions:

            #if w in node.children: 

            # tmp = w
            path = path + w
            board[i][j]= '#'
            node = node.children[w]
            dfs(board, i+1, j, node, path)
            dfs(board, i-1, j, node, path)
            dfs(board, i, j+1, node, path)
            dfs(board, i, j-1, node, path)
            # board[i][j] = tmp
            board[i][j] = w
        #### end of dfs
        
        trie = Trie()
        res = []
        for x in words: 
            trie.insert(x)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, i, j, trie.root, '')

        return res