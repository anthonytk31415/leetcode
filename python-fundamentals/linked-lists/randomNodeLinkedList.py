# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from random import randint

class Solution:

    def __init__(self, head):
        self.head = head
        self.length = None
        self.getLength()

    def getLength(self):
        node = self.head
        counter = 0
        while node:
            node = node.next
            counter +=1
        self.length = counter
        return 

    def getRandom(self) -> int:
        n = randint(0, self.length - 1)
        node = self.head
        for _ in range(n):
            node = node.next
        return node.val
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

sol = Solution(head)
print(sol.getRandom())