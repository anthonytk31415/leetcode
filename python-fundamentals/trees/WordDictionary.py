class WordDictionary:

    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

    def addWord(self, word: str) -> None:
        # print(f'inserting {word}')
        if self.val == None: # base case where the word dictionary is empty
            self.val = word
            return
        # traverse the tree to find a node to enter; do until you find a left/right == None
        x = self
        while x != None:
            # print(x)             
            if word < x.val:
                if x.left == None: 
                    x.left = WordDictionary()
                    x.left.val = word
                    return  
                else: 
                    x = x.left
            else: 
                if x.right == None: 
                    x.right = WordDictionary()
                    x.right.val = word
                    return
                else: 
                    x = x.right

    def search(self, word: str) -> bool:

        def pureSearch(self, word):
            x = self
            while x != None:
                if x.val == word:
                    return True
                if word < x.val:
                    x = x.left
                else:
                    x = x.right
            return False

        def dotSearch(self, word):
            def check(dictWord, word):
                if len(dictWord) != len(word):
                    return False
                for i in range(len(word)):
                    if word[i] == '.':
                        continue
                    if word[i] != dictWord[i]:
                        return False
                return True
            
            x = self
            while x != None:
                if check(self.val, word):
                    return True
                else:

        

        if '.' in word:
            return dotSearch(self, word)
        else:
            return pureSearch(self, word)

wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print(wd.val)
print(wd.right.right.val)
print(wd.right.val)

print(wd.search('mad'))
print(wd.search('dad'))
print(wd.search('sad'))
# x = 5
# if 1 > 4: x = 3
# else: x = 99
# print(x)

# ..a. [aaaa, zzaz] = min, max

# bane
# ba.l--> range = [baal, bazl]; if outside range, then not equal; else, 
# left --> range = [baal, bane] i.e. [old min, new max = node val]
# right --> range = [bane, bazl] i.e.[new min = node val, old max]
# say you go (1) right: base --> True
#                      bazx --> out of range --> go left
# (2); right: xxct --> out of range, go left
# do this until you get to a null node, if null: false