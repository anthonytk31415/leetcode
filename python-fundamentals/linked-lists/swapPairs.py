# swapPairs
# Definition for singly-linked list.

# Time: O(N)
# Space: O(1) 

# a cool trick: instead of worrying about which node to attach, do it at the same time in a one liner!
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    newHead = ListNode()
    prev = newHead
    cur = head
    while cur: 
        if cur and cur.next:
            attachNext = cur.next.next
            prev.next = cur.next
            prev.next.next = cur

            prev = prev.next.next
            cur = attachNext
        elif cur and not cur.next:
            prev.next = cur
            prev = prev.next
            cur = cur.next
    prev.next = None
    return newHead.next


def swapPairs2(head):
    newHead = ListNode()
    prev = newHead
    cur = head
    while cur: 
        if cur and cur.next:
            n2 = cur.next
            n1 = cur
            cur = cur.next.next
            prev.next, n2.next, = n2, n1
            prev = n1
        elif cur and not cur.next:
            prev.next, cur = cur, cur.next
    prev.next = None
    return newHead.next





def traverse(head):
    node = head
    while node: 
        print(node.val)
        node = node.next

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

new = swapPairs2(node)
# print(new.val)
# traverse(node)
traverse(new)