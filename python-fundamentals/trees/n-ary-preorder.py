"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        res = []
        if root:
            res.append(root.val)
            for child in root.children:
                res = res + self.preorder(child)
        return res