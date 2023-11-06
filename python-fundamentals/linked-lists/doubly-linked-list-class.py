class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, val):
        newHead = Node(val)
        newHead.next = self.head
        if self.head: 
            self.head.prev = newHead
        self.head = newHead

    def addToTail(self, val):
        newNode = Node(val)
        node = self.head
        # traverse to end
        while node.next:
            node = node.next
        node.next = newNode
        newNode.prev = node

    def traverse(self):
        node = self.head
        while node: 
            print(node.val)
            node = node.next

    def intoAndOut(self):
        node = self.head
        if node: print(node.val)
        while node.next: 
            node = node.next
            print(node.val)
        while node.prev:
            node = node.prev
            print(node.val)

root = DoublyLinkedList()
root.addToHead(1)
root.addToHead(0)
root.addToTail(2)
root.addToTail(3)
root.addToTail(4)
root.intoAndOut()



## double
# add to head: O(1)
# add to tail: O(n)

# ## single: 
# add to head: O(1)
# add to tail: O(n)