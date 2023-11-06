class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from math import inf

def pairSum(head):
    
    def lengthLinkedList(head):
        n = 0
        cur = head
        while cur: 
            n += 1
            cur = cur.next
        return n

    n = lengthLinkedList(head)
    # print(n)
    # split the linked list into two
    # for the second one, reverse it

    firstHalf = ListNode()
    firstHalf.next = head
    cur = head
    prev = None
    for _ in range(n//2):
        prev = cur
        cur = cur.next

    prev.next = None


    # now reverse
    secondHalf = ListNode()
    prev = None
    post = None
    for _ in range(n//2):
        if cur.next: 
            post = cur.next
        else: 
            post = None

            
        cur.next = prev
        prev = cur 
        cur = post
    secondHalf.next = prev

    res = -inf 
    cur1 = firstHalf.next
    cur2 = secondHalf.next
    for _ in range(n//2):
        curSum = cur1.val + cur2.val
        res = max(res, curSum)
        cur1, cur2 = cur1.next, cur2.next
    return res

head = ListNode(1)
head.next = ListNode(7)
head.next.next = ListNode(101)
head.next.next.next = ListNode(99)

arr = pairSum(head)
print(arr)
# for node in arr: 
#     cur = node
#     print("start print")
#     while cur: 
#         print(cur.val)
#         cur = cur.next
