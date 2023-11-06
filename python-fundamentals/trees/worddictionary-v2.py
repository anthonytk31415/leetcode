class WordNode:
    def __init__(self) -> None:
        self.word = None
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = WordNode()
            node = node.children[w]
        node.word = True

    # using while statements
    # def search(self, word: str) -> bool:
    #     stack = [(self.root, 0)]
    #     while stack:
    #         (node, i) = stack.pop()
    #         if i == len(word):
    #             if node.word == True:
    #                 return True
    #         else: 
    #             w = word[i]
    #             if w == '.':
    #                 for c in node.children:
    #                     stack.append((node.children[c], i + 1))
    #             elif w in node.children:
    #                 stack.append((node.children[w], i + 1))
    #     return False
    
    # using recursion 
    def search(self, word: str) -> bool:
        def dfs(root, word):
            node = root
            if len(word) == 0:
                if node.word == True:
                    return True
                else: 
                    return False
            w = word[0]
            if w == '.':
                return any([dfs(node.children[w], word[1:]) for w in node.children])
            elif w in node.children:
                return dfs(node.children[w], word[1:])
            else: 
                return False
        return dfs(self.root, word)



# search without the '.' notation
    # def search(self, word: str) -> bool:
    #     node = self.root
    #     for w in word: 
    #         if w not in node.children:
    #             return False
    #         node = node.children[w]
    #     return node.word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# wd = WordDictionary()
# wd.addWord("bad")
# wd.addWord("dad")
# wd.addWord("mad")
# print(wd.search2("pad")) #// return False
# print(wd.search2("bad")) #// return True
# print(wd.search2(".ad")) #// return True
# print(wd.search2("b..")) #// return True

wd = WordDictionary()
wd.addWord("a")
wd.addWord("a")
# print(wd.root.children['a'].word)
print(wd.search("a"))
# print(wd.search("."))
# print(wd.search(""))
# print(wd.search(".a"))

# print(wd.search("aa"))






##### crap below

    # def search(self, word: str) -> bool:
    #     node = self.root
    #     stack = []
    #     i = 0
    #     w = word[0]
    #     ## initial conditions: get something in the stack, or return false
    #     if w == '.':
    #         for child in node.children:
    #             stack.append((node, i, child))
    #     elif w not in node.children:
    #         return False 
    #     else: 
    #         stack.append((node, i, w))  

    #     while len(stack)>0:
    #         # traverse to the next node and pop the stack
    #         (a,b,c) = stack.pop()
    #         node = a
    #         i = b
    #         # print(f'children appended: {c}')
    #         child = c
    #         # print(child)
    #         node = node.children[child]
    #         i +=1     

    #         # print(len(word), i)
    #         # now reload the stack with a singular child if w in children, or for each child in children if w = '.'
    #         if len(word) == i:
    #             # print(node.word)
    #             # print(stack)
    #             if node.word == True:
    #                 return True
    #         ## conditions: i < len(word) or node.word == False -> pop the stack :
    #         if i < len(word):
    #             w = word[i]
    #             if w == '.':    
    #                 for child in node.children.keys(): 
    #                     stack.append((node, i, child))
    #             elif w in node.children:
    #                 stack.append((node, i, w))

           
    #     return node.word