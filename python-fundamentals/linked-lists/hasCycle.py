# hasCycle

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def print(self):
        node = self
        while node:
            print(node.val)
            node = node.next

cycle = ListNode(2)

node = ListNode(3)
node.next = cycle
node.next.next = ListNode(4)
node.next.next.next = ListNode(6)
node.next.next.next.next = cycle

# node.print()

mydict = set()
mydict.add(node)
print(mydict)

def hasCycle(head):
    lookup = set()

    while head:
        if head not in lookup:
            lookup.add(head)
        else:
            return True
        head = head.next
    return False

print(hasCycle(node))