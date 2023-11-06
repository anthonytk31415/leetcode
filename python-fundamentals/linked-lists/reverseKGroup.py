# Time: O(n)
# Space: O(1)!!!

# tip: we might have extra pointers, but for now, we have: 
# - a cycle head, cycle tail, 
# - dummy to keep track of the returning head
# - main tail to attach the new cycle to (previous cycle: attach at the main tail the new cycle, and redefine the new main tail to the end of that cycle)
# - cur and prev to attach nodes together, 
# - node to keep track of where you are as you traverse the root
# - each cycle will attach nodes between the c_head and c_cycle: head > 3,2,1 and tail will refer to the first node you attach
# - before each cycle, check if a cycle exists; if not, then just return the next node to the end of the main tail 

## biggest tip: draw a picture and the iteration of what you want to happen!!!


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def check(root, k):
    node = root
    for _ in range(k-1):
        if not node.next:
            return False
        else: 
            node = node.next
    return True

def reverseKGroup(head, k):
    c_head = ListNode(0)
    c_tail = head
    prev = c_tail
    c_head.next = c_tail
    dummy = main_tail = ListNode(0)
    node = head
    while node and check(node, k):
        for _ in range(k):
            cur = node
            c_head.next = cur
            node = node.next
            cur.next = prev
            prev = cur 
        main_tail.next = c_head.next
        main_tail = c_tail
        c_tail = node 
    main_tail.next = node
    return dummy.next 



root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(6)
root.next.next.next.next.next.next = ListNode(7)
root.next.next.next.next.next.next.next = ListNode(8)

z = reverseKGroup(root, 3)
print(z.val)
print(z.next.val)
print(z.next.next.val)
print(z.next.next.next.next.next.next.val)