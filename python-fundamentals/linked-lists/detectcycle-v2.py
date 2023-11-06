# detectcycle

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectcycle(head):
    # each node: input the val and index in dictionary
    lookup = {}
    node = head
    index = 0
    while node:
        # print(node.val)
        if node.val not in lookup:
            lookup[node.val] = [(node, index)]
        else: 
            for x in lookup[node.val]:
                if x[0] == node:
                    return node
            lookup[node.val].append((node, index))
        node = node.next
        index += 1
    return -1




x = ListNode(1)
a1 = ListNode(2)
a2 = ListNode(3)
a3 = ListNode(4)
a4 = ListNode(5)

x.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a2

# print(x.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.val)


print(detectcycle(x))