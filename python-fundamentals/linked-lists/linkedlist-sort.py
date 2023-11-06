# linkedlist sort

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# this uses sorting functions at time = O(n log n) time, but storage O(n)
def sortList(head):
    arr = []
    node = head
    while node:
        arr.append(node.val)
        node = node.next
    arr=sorted(arr)
    
    dummy = ListNode()
    cur = dummy
    for i in range(len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return dummy.next


# uses linked lists; 
# Time = O(n log n); Space = uses O(log N)
def sortList2(head):
    if not head or not head.next:
        return head

    def getMid(head):           # fast starts at head.next; returns median or lower of median; mergesort will take 1 + median for right
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def mergesort(left, right):
        tail = dummy = ListNode()
        while left and right: 
            if left.val < right.val: 
                tail.next = left
                left = left.next
            else: 
                tail.next = right
                right = right.next
            tail = tail.next
        while left: 
            tail.next = left
            left = left.next
            tail = tail.next
        while right:
            tail.next = right
            right = right.next
            tail = tail.next
        return dummy.next
    
    #define left and right; cut off the mid part for left
    left = head
    right = getMid(head)
    tmp = right.next
    right.next = None
    right = tmp

    leftL = sortList2(left)
    rightL = sortList2(right)

    return mergesort(leftL, rightL)




    