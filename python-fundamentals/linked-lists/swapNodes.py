class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head, k):

    dummy_head = ListNode()         # this points to the head
    dummy_head.next = head          

    node = dummy_head
    n = 0

    # First, find the kth node, prev_k, and k_next
    while node and node.next: 
        node = node.next
        n +=1
        if n == k: 
            k_node = node 

    node = dummy_head
    for _ in range(n - k + 1):
        node = node.next

    node.val, k_node.val = k_node.val, node.val
    return dummy_head.next

    # print(n)
    # print('prev_k', prev_k.val)
    # print('k', k_node.val)
    # print('knext', k_next.val)
    # print('prev nk: ', prev_n_k_node.val)
    # print('nk', n_k_node.val)
    # print('nk next: ', nk_next.val)
    # if n == 1: 
    #     return dummy_head.next

# head = [7,9,6,6,7,8,3,0,9,5], k = 5

# head = ListNode(7)
# head.next = ListNode(9)
# head.next.next = ListNode(6)
# head.next.next.next = ListNode(6)
# head.next.next.next.next = ListNode(7)
# head.next.next.next.next.next = ListNode(8)
# head.next.next.next.next.next.next = ListNode(3)
# head.next.next.next.next.next.next.next = ListNode(0)
# head.next.next.next.next.next.next.next.next = ListNode(9)
# head.next.next.next.next.next.next.next.next.next = ListNode(5)

head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
# head.next.next.next.next.next.next.next = ListNode(8)
# head.next.next.next.next.next.next.next.next = ListNode(9)
# head.next.next.next.next.next.next.next.next.next = ListNode(10)
# head = ListNode(1)

z = swapNodes(head, 2)

print(z.val)
print(z.next.val)
# print(z.next.next.val)
# print(z.next.next.next.val)
# print(z.next.next.next.next.val)
# print(z.next.next.next.next.next.val)
# print(z.next.next.next.next.next.next.val)
# print(z.next.next.next.next.next.next.next.val)
# print(swapNodes(head, 2))

# node = z
# while node: 
#     print(node.val)
#     node = node.next
