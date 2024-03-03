class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode()
    dummy.next = head
    node = dummy
    countNodes = 0
    while node: 
        node = node.next
        countNodes += 1
    
    node = dummy
    for _ in range(countNodes - n -1):
        node = node.next
    node.next = node.next.next
    return dummy.next

x = ListNode(1)
# x.next = ListNode(2)
# x.next.next = ListNode(3)
# x.next.next.next = ListNode(4)
# x.next.next.next.next = ListNode(5)

y = removeNthFromEnd(x, 2)
while y: 
    print(y.val)
    y = y.next