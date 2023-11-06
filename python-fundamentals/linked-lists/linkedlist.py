# linked list 


class LinkedListIterator:
    def __init__(self, head):
        self._current = head
    
    def __iter__(self):
        return self 
    
    def _next__(self):
        if self._current == None:
            raise StopIteration
        else: 
            value = self._current.value 
            self._current = self._current.next
            return value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1
        return self


    def __iter__(self):
        return LinkedListIterator(self.head)




z = Node(1)
print(z.next)

linked_list = LinkedList()
linked_list.add('node 1')
linked_list.add('node 2')
linked_list.add('node 3')
linked_list.add('node 4')
linked_list.add('node 5')

# for x in linked_list:
#     print(x)




def reverseList(node):
    if not node:
        return node
    prev = None
    new = node
    tempnext = node.next
    new.next = prev
    while tempnext:
        prev = node
        node = tempnext
        new = node
        tempnext = node.next
        new.next = prev
    return new


def printNodes(node):
    x = node
    while x:
        print(x.value)
        x = x.next

rev = reverseList(linked_list.head)
printNodes(rev)
# printNodes(linked_list.head)