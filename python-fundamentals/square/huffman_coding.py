# 952
from collections import Counter

def frequency(s):
    return Counter(s)
s = "aabbbbbcDDD"
print(frequency(s))


class TreeNode:
    def __init__(self, val = None, char = None):
        self.char = char
        self.val = val
        self.left = None
        self.right = None

def makeTree(s):
    freq = frequency(s)
    ## create an array that is sorted min first
    freq_sorted = [(freq[x], x) for x in freq]
    freq_sorted.sort(key=lambda x: x[0])            # freq_sorted[i] = (count, char)


    ## then iterate over the array and build the tree
    if not freq_sorted: 
        return TreeNode()
    if len(freq_sorted) == 1: 
        return TreeNode(freq_sorted[0][0], freq_sorted[0][1])

    cur_val = freq_sorted[0][0] + freq_sorted[1][0]
    dummy = TreeNode(cur_val, '#')
    dummy.right = TreeNode(freq_sorted[0][0], freq_sorted[0][1])
    dummy.left = TreeNode(freq_sorted[1][0], freq_sorted[1][1])
    freq_sorted = freq_sorted[2:]
    while freq_sorted: 
        cur_left = TreeNode(freq_sorted[0][0], freq_sorted[0][1])
        cur_val = cur_val + freq_sorted[0][0]
        cur = TreeNode(cur_val, '#')
        cur.left = cur_left
        cur.right = dummy
        dummy = cur 
        freq_sorted = freq_sorted[1:]

    return dummy


def traversal(root):
    res = []
    if not root: 
        return res
    else: 
        res = res + traversal(root.left)
        res.append((root.val, root.char))
        return res + traversal(root.right)

root = makeTree(s)
print(traversal(root))


def path_map(root):
    char_map = {}

    # single root node condition
    if root.char != '#':
        return {root.char: '1'}
    
    def helper(root, char_map, path):
        if root.char != '#': 
            char_map[root.char] = path
            return 
        else: 
            helper(root.left, char_map, path + '0')
            helper(root.right, char_map, path + '1')

    helper(root, char_map, '')
    return char_map

print(path_map(root))

# root_1 = makeTree('a')
# print(path_map(root_1))


def str_to_comp(s):
    root = makeTree(s)
    path = path_map(root)
    res = ''
    for c in s: 
        res = res + path[c]
    return res

compr = str_to_comp(s)
print(str_to_comp(s))

#errors: 
# tree hits more chars than is allowed in the tree; or less
# 

def comp_to_string(code, tree):
    def helper(code, tree):

        s = ''
        # handle null values
        if not code: 
            return s

        node = tree
        # handle trees of one node; code should be all '1's 

        ## do operations until you get to a leaf
        while code != '':         

        ## traverse the node
            cur_dir = code[0]
            code = code[1:]
            if cur_dir == '1': 
                node = node.right
            else: 
                node = node.left  

        # evalulate leaf condition; do some error checking
            if node.char != '#':
                if node.val == 0: 
                    print('fail 1')
                    return Exception('Invalid Code: not enough chars in tree; too many chars asked in code')
                node.val -=1
                s = s + node.char
                node = tree

        ## if at the end you are not at the top of the tree --> invalid
        if node != tree: 
            print('fail 2')
            return Exception('Invalid Code: instructions landed you in the middle of the tree')

        return s

    try: 
        return helper(code, tree)
    except: 
        print("This is an invalid compressed string.")


print(comp_to_string(compr, root))