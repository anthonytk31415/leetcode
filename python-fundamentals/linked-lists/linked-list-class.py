# linked list practice

class LinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, val):
        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead

    def addToTail(self, val):
        newTail = Node(val)
        node = self.head
        while node.next: 
            node = node.next
        node.next = newTail

    def traverse(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# class DNode(Node):
#     def __init__(self, val):
#         super().__init__(self, val)
#         self.prev = None


# root = DNode(3)



# root = LinkedList()
# root.addToHead(1)
# root.addToHead(0)
# root.addToTail(2)
# root.addToTail(3)
# root.addToTail(4)
# root.traverse()