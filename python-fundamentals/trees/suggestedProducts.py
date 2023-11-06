from collections import defaultdict
# from bisect import bisect

# Time: O(nlogn) for sorting the words in lexicographical order
# Space: O(total chars) for the trie

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.words = []


def insertWord(cur_word, node, word):
    node.words.append(word)
    if not cur_word: 
        return
    else:
        return insertWord(cur_word[1:], node.children[cur_word[0]], word)

def wordTree(word, node):
    res = []
    i = 0
    while i < len(word):
        node = node.children[word[i]]
        cur_res = [x for x in node.words]
        cur_res.sort()
        res.append(cur_res[:3])
        i +=1
    return res

def suggestedProducts(products, searchWord):
    dictionary = Node()
    for product in products: 
        insertWord(product, dictionary, product)
    
    return wordTree(searchWord, dictionary)

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(suggestedProducts(products, searchWord))




