class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n)
# Space: O(1)

def partition(head, x):
    small, big = ListNode(), ListNode()
    cur_small, cur_big = small, big
    node = head

    while node: 
        if node.val >= x: 
            cur_big.next = node 
            cur_big = cur_big.next
        else: 
            cur_small.next = node
            cur_small = cur_small.next

        node = node.next

    cur_small.next = big.next
    cur_big.next = None

    return small.next