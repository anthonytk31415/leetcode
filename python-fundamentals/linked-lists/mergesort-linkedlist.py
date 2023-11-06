# mergesort with linkedlists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getmid(lst):
    slow = lst
    fast = lst.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def mergesort(lst):
    if not lst or not lst.next: 
        # traverse(lst)
        # print('---')
        return lst
    q = getmid(lst)
    left = lst
    tmp = q.next
    q.next = None
    right = tmp
    # traverse(left)
    # traverse(right)
    # print('---')
    left1 = mergesort(left)
    right1 = mergesort(right)
    return merge(left1, right1)


def merge(left, right):
    # print(left, right)
    dummy = node = ListNode()
    while left and right:
        if left.val < right.val:
            node.next = left
            left = left.next
        else: 
            node.next = right
            right = right.next
        node = node.next
    if left: 
        node.next = left 
        # left = left.next
        # node = node.next
    if right:
        node.next = right
        # right = right.next
        # node = node.next
    return dummy.next

def traverse(root):
    node = root
    while node:
        print(node.val)
        node = node.next

root = ListNode(9)
root.next = ListNode(3)
root.next.next = ListNode(1)
root.next.next.next = ListNode(2)
root.next.next.next.next = ListNode(22)
# traverse(root)
z= mergesort(root)
# print(z)
traverse(z)


# print(getmid(root).val)