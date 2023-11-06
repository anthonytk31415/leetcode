# mergeKLists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        node = self
        while node:
            print(node.val)
            node = node.next


def merge(a,b):
    nodeA, nodeB = a, b
    dummy = cur = ListNode()
    while nodeA and nodeB:
        if nodeA.val < nodeB.val:
            cur.next = nodeA
            nodeA = nodeA.next
        else:
            cur.next = nodeB
            nodeB = nodeB.next
        cur = cur.next
    if nodeA:
        cur.next = nodeA
    if nodeB: 
        cur.next = nodeB
    return dummy.next



def mergeKLists(lists):
    if len(lists) == 0:
        return None    
    elif len(lists) == 1:
        return lists[0]
    mid = len(lists)//2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    merged = merge(left, right)
    return merged






# ////////
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



nodeA = ListNode(1)
nodeA.next = ListNode(2)
nodeA.next.next = ListNode(3)
nodeA.next.next.next = ListNode(5)
nodeA.next.next.next.next = ListNode(10)
nodeA.next.next.next.next.next = ListNode(20)

nodeB = ListNode(3)
nodeB.next = ListNode(4)
nodeB.next.next = ListNode(6)
nodeB.next.next.next = ListNode(7)
nodeB.next.next.next.next = ListNode(8)
nodeB.next.next.next.next.next = ListNode(29)
nodeB.next.next.next.next.next.next = ListNode(30)
nodeB.next.next.next.next.next.next.next = ListNode(31)


nodeC = ListNode(19)
nodeC.next = ListNode(20)
nodeC.next.next = ListNode(22)
nodeC.next.next.next = ListNode(24)
nodeC.next.next.next.next = ListNode(27)
nodeC.next.next.next.next.next = ListNode(39)

lists = [nodeA, nodeB, nodeC]

# x = merge(nodeA, nodeB)
# x.print()

z = mergeKLists(lists)
print(z)
z.print()