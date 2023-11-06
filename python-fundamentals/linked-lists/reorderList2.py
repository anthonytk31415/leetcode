from collections import deque 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    arr = deque()
    node = head
    while node: 
        arr.append(node)
        node = node.next
    

    dummy = ListNode()
    front = True
    node = dummy
    while arr: 
        if front: 
            node.next = arr.popleft()
        else: 
            node.next = arr.pop()
        front = not front
        node = node.next
    node.next = None
    return dummy.next


# using constant space: 


## e.g. 1,2,3,4,5
# returns 3
# for even: 1,2,3,4
# returns 2
def findMid(head):
    fast = head
    slow = head 
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def reorderList(head):
    # find the mid; if it's even, return the 
    mid = findMid(head)

    # get the first half 
    

    # get the second half and reverse the list


    # now merge by alternating
