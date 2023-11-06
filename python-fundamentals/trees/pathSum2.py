# pathSum2

# this is the same concent as pathSum1, however you'll return all valid paths to the sum rather than just true or false
# - the trick is how you do so. if you do so recursively, each fork  via recursion can call a res and append the path 
# - It's a good practie to do BFS or DFS
# - for BFS, if the current node (starting with root, then recursively running down) is not null: then apply the Target Sum - val, then add that node to the path

# some things to worry about: 
# - beware of the path you return if you code a recursive function and pass the same path in recursive arguments; if it's the same name, when you append
#   stuff, it'll append globally so you need to somehow create a copy and pass that as an argument

# this runs O(n) running time for all the nodes potentially and O(1) for storage 


class Node: 
    def __init__ (self, val = None): 
        self.val = val
        self.left = None
        self.right = None

    def preorderTraversal(root):
        res = []
        if root: 
            res.append(root.val)
            res = res + Node.preorderTraversal(root.left)
            return res + Node.preorderTraversal(root.right)
        else: 
            return res

def pathsum(root, targetSum):
    container = []
    def helper(root, targetSum, path=[]):
        curPath = [x for x in path]
        if root:
            targetSum -= root.val 
            curPath.append(root.val)

            if root.left == None and root.right == None:
                if targetSum == 0: 
                    container.append(curPath)
                    # print(curPath)
                    return 
                else: 
                    return 
            else: 
                # print(path)
                helper(root.left, targetSum, curPath)
                helper(root.right, targetSum, curPath)

        else: 
            # print(curPath)
            return 

    helper(root, targetSum, [])
    return container


## another solution 

def pathsum2(root, targetSum):
    def dfs(root, ts, path, res):
        if root: 
            ts -= root.val
            if not root.left and not root.right and ts == 0:
                path.append(root.val)
                res.append(path)
            else: 
                dfs(root.left, ts, path + [root.val], res)
                dfs(root.right, ts, path + [root.val], res)

    res = []
    dfs(root, targetSum, [], res)
    return res

## using a dfs stack
def pathsumDFS(root, targetSum):
    res = []
    if not root:
        return res
    stack = [(root, targetSum - root.val, [root.val])]
    while stack:
        node, ts, path = stack.pop()
        print(ts, path)
        if not node.left and not node.right and ts == 0: 
            res.append(path)
        if node.left: 
            stack.append((node.left, ts - node.left.val, path + [node.left.val]))
        if node.right: 
            stack.append((node.right, ts - node.right.val, path + [node.right.val]))
    return res

## using a bfs queue
def pathsumBFS(root, targetSum):
    res = []
    if not root: 
        return res
    queue = [(root, targetSum - root.val, [root.val])]
    while queue: 
        node, ts, path = queue.pop(0)
        if not node.left and not node.right and ts == 0:
            res.append(path) 
        for x in [node.left, node.right]:
            if x: 
                queue.append((x, ts - x.val, path + [x.val]))
    return res



root = Node(10)
root.left = Node(5)
root.left.left = Node(1)
root.left.right = Node(7)
root.right = Node(12)
root.right.left = Node(11)
root.right.right = Node(-6)
# 10, 5, 1, 7, 12, 11, -6

# print(Node.preorderTraversal(root))


print(pathsumBFS(root, 16))



## 16