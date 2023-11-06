# oddEvenList
# Time: O(N)
# Space: O(1) additional space (use the constant time for pointers, reassign existing nodes to new "nexts")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## using pointers
def oddEvenList(head):
    fres, sres = ListNode(), ListNode()
    cur = head
    first, second = fres, sres
    while cur and cur.next:
        first.next = cur
        first = first.next
        second.next = cur.next
        second = second.next
        cur = cur.next.next
    if cur: 
        first.next = cur
        first = first.next
        second.next = None
        second = second.next

    first.next = sres.next
    return fres.next

    # build list of all odds
    # biuld list of all evens

    # while both are true, alternate in a loop

    # at the end, attach them together

## rewrite for even more compact version

def oddEvenList2(head):
    if not head: 
        return head
    dum = ListNode()
    dum.next = odd = head # will return the head
    evenHead = even = head.next
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = evenHead
    return dum.next


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)

def traverse(root):
    node = root
    while node: 
        print(node.val)
        node = node.next



new = oddEvenList2(root)
traverse(new)

# 1,3,5,2,4