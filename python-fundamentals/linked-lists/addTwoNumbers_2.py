class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import deque
def addTwoNumbers(l1, l2):

    node1 = l1
    node2 = l2
    len_n1, len_n2 = 1, 1
    rest = []
    for node, len_n in [(node1, len_n1), (node2, len_n2)]:
        print((node.val, node.next))
        while node.next:
            print(node.val)
            node = node.next
            len_n +=1
        print('final-len', len_n)
        rest.append(len_n)

    print('len of lengths', rest)


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(4)
l2.next = ListNode(5)
l2.next.next = ListNode(6)
l2.next.next.next = ListNode(7)

print('blah', addTwoNumbers( l1, l2))