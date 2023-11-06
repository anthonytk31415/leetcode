# Write your class here.
## implementing a manual __iter__ and __next__



class LinkedListIterator:
    def __init__(self, _head):
        self._current = _head
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self._current == None:
            raise StopIteration
        else: 
            value = self._current._value 
            self._current = self._current._next
            return value


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def add(self, value):
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
        else:
            self._tail._next = new_node

        self._tail = new_node
        self._length += 1
        return self


    def __iter__(self):
        return LinkedListIterator(self._head)







def reverseList(node):
    prev = None
    new = node
    temp_next = node.next
    new.next = prev
    while temp_next:
        prev = node
        node = temp_next
        new = node
        temp_next = node.next
        new.next = prev
    return new




linked_list = LinkedList()
linked_list.add('node 1')
linked_list.add('node 2')
linked_list.add('node 3')
linked_list.add('node 4')
linked_list.add('node 5')