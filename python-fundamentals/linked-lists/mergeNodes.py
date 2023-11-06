# mergeNodes
# 11 min solved

# Time: O(n)
# Space: O(n) for the new list
# you could store this in an old node to make it O(1) and make it more confusing
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head):
    dummy = ListNode() 
    newNode = dummy
    cur = head.next
    curSum = 0
    while cur: 
        if cur.val !=0:
            curSum += cur.val
            cur = cur.next 
        else:   # cur.val == 0
            newNode.next = ListNode(curSum)
            newNode = newNode.next

            curSum = 0
            cur = cur.next
    return dummy.next