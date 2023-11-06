from collections import defaultdict, deque
from math import inf

class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = defaultdict(TreeNode)
        self.parent = None
    
    @staticmethod
    def insert(node, val):
        # print(val)
        if node.val == None or node.val % val == 0 or val % node.val == 0:
            if not node.children: 
                newNode = TreeNode(val)
                newNode.parent = node
                node.children[val] = newNode

            else: 
                div_child = False
                for child in node.children: 
                    # print('child', child)
                    if child % val == 0 or val % child == 0:
                        TreeNode.insert(node.children[child], val)
                        div_child = True
                if div_child == False: 
                    newNode = TreeNode(val)
                    newNode.parent = node
                    node.children[val] = newNode

    @staticmethod
    def inorderTraversal(node):
        res = []
        if not node: 
            return res
        else: 
            res.append(node.val)
            for child in node.children: 
                res = res + TreeNode.inorderTraversal(node.children[child])
            return res
    
    @staticmethod
    def findDeepest(node):        
        counter = 0
        queue = deque()
        queue.append(node)
        while queue: 
            counter +=1
            for _ in range(len(queue)):
                curNode = queue.popleft()
                for child in curNode.children: 
                    queue.append(curNode.children[child])
        return counter, curNode

    @staticmethod
    def trace(node):
        res = []
        curNode = node
        while curNode: 
            if curNode.val != None:
                res.append(curNode.val)
            curNode = curNode.parent

        return res[::-1]


# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         f = TreeNode()
#         for x in nums: 
#             TreeNode.insert(f, x)
#         count, deep = TreeNode.findDeepest(f)
#         return TreeNode.trace(deep)

# def largestDivisibleSubset(nums):
#     pass

f = TreeNode()

# TreeNode.insert(f, 1)
# TreeNode.insert(f, 3)
# TreeNode.insert(f, 5)
# TreeNode.insert(f, 6)
# TreeNode.insert(f, 12)
# TreeNode.insert(f, 15)
# TreeNode.insert(f, 18)

# # print(f.children[1].children[3].children[6].children[18].parent.val)
# # print(f.children[1].parent.val)
# print(f.children[1].children[3].parent.val)
# print(TreeNode.inorderTraversal(f))
# count, deep = TreeNode.findDeepest(f)

# print(TreeNode.trace(deep))




def largestDivisibleSubset(nums):
    nums.sort()
    res = []                # res[i] = (num, count of div)
    for x in nums: 
        print(x)
        print(res)
        if not res: 
            res.append([[x], 1])
        else: 
            curCount = -inf
            curIdx = None
            for i, (arr, count) in enumerate(res): 
                num = arr[-1]
                if x % num == 0 and curCount < count: 
                    curCount = count
                    curIdx = i
            if curIdx != None: 
                arr, cnt = res[curIdx]
                res.append([arr + [x], cnt + 1])
            else:                 
                res.append([[x], 1])
    
    print(res)
    maxCount = -inf
    resArr = None
    for (arr, count) in (res):
        if count > maxCount: 
            maxCount = count
            resArr = arr
    return resArr

# nums = [1,2,4,8]
# nums = [3,4,16,8]
nums = [4,8,10,240]
print(largestDivisibleSubset(nums))