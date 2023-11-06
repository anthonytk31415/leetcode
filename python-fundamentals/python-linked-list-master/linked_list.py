"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""

# Phase 1

# TODO: Implement a Linked List Node class here
class Node:
  # TODO: Set the `_value` `_next` node instance variables
  def __init__(self, value):
    self._value = value
    self._next = None


# TODO: Implement a Singly Linked List class here
class LinkedList:
  """ this is a linked list"""
  def __init__(self):
    self._head = None
    self._tail = None
    self._length = 0

  # TODO: Implement the get_node method here
  def get_node(self, position):
    pass
    cur = self._head
    i = 0
    while i < position:
      if cur == None:
        return None
      else:
        cur = cur._next
        i +=1
    return cur

  # TODO: Implement the add_to_tail method here
  def add_to_tail(self, value):
    newNode = Node(value)
    if self._head == None:
      self._head = newNode
    else:
      self._tail._next = newNode
    self._tail = newNode
    self._length +=1
    return self

  # TODO: Implement the add_to_head method here
  def add_to_head(self, value):
    newNode = Node(value)
    if self._head == None:
      self._tail = newNode
    newNode._next = self._head
    self._head = newNode  
    self._length +=1
    return self

  # TODO: Implement the remove_head method here
  def remove_head(self):
    if self._head == None:
      return None
    else:
      newHead = self._head._next
      oldHead = self._head
      self._head = newHead
      self._length -=1
      if self._length == 0:
        self._tail ==None
      return oldHead

  # TODO: Implement the remove_tail method here
  def remove_tail(self):
    if self._head == None:
      return None
    elif self._length == 1:
      oldTail = self._tail
      self._head = None
      self._tail = None
    else:
      oldTail = self._tail
      self._tail = self.get_node(self._length-1)
      self._tail._next = None
    self._length -=1
    return oldTail

  # TODO: Implement the __len__ method here
  def __len__(self):
    return self._length

# Phase 2

  # TODO: Implement the contains_value method here
  def contains_value(self, target):
    cur = self._head
    while cur != None:
      if cur._value == target:
        return True
      cur = cur._next
    return False

  # TODO: Implement the insert_value method here
  def insert_value(self, position, value):
    if position > self._length or position < 0:
      return False
    elif position == 0:
      self.add_to_head(value)
    elif position == self._length:
      self.add_to_tail(value)
    else:
      node_before_insert = self.get_node(position)
      insert = Node(value)
      node_after_insert = node_before_insert._next
      node_before_insert._next = insert
      insert._next = node_after_insert
      self._length +=1
    return True

  # TODO: Implement the update_value method here
  def update_value(self, position, value):
    if position > self._length or position < 0:
      return False
    else:
      cur = self.get_node(position)
      cur._value = value
      return True

  # TODO: Implement the remove_node method here
  def remove_node(self, position):
    if position > self._length or position < 0:
      return False
    elif position == 0:
      return self.remove_head()
    elif position == self._length:
      return self.remove_tail()
    else:
      node_before_position = self.get_node(position-1)
      node_to_remove = node_before_position._next
      node_for_next = node_before_position._next._next
      node_before_position._next = node_for_next
      self._length -=1
      return node_to_remove


  # TODO: Implement the __str__ method here
  def __str__(self):
    return f'this is a LinkedList with length = {self._length}.'

# Phase 1 Manual Testing:

# # 1. Test Node and LinkedList initialization
# node = Node('hello')
# print(node)                                     # <__main__.Node object at ...>
# print(node._value)                              # hello
# linked_list = LinkedList()
# print(linked_list)                              # <__main__.LinkedList object at ...>

# # # 2. Test getting a node by its position
# print(linked_list.get_node(0))                # None

# # # 3. Test adding a node to the list's tail
# linked_list.add_to_tail('new tail node')
# print(linked_list.get_node(0))                # <__main__.Node object at ...>
# print(linked_list.get_node(0)._value)         # `new tail node`

# # # 4. Test adding a node to list's head
# linked_list.add_to_head('new head node')
# print(linked_list.get_node(0))                # <__main__.Node object at ...>
# print(linked_list.get_node(0)._value)         # `new head node`


# print(linked_list._length)
# print(linked_list._tail._value)
# print(linked_list._head._value)
# print(linked_list._head._next._value)

# # # 5. Test removing the head node
# linked_list.remove_head()
# print(linked_list.get_node(0)._value)         # `new tail node` because `new head node` has been removed
# print(linked_list.get_node(1))                # `None` because `new head node` has been removed

# # # 6. Test removing the tail node
# print(linked_list.get_node(0)._value)         # `new tail node`
# linked_list.remove_tail()
# print(linked_list.get_node(0))                # None

# # # 7. Test returning the list length
# print(len(linked_list))                                 # 2


# linked_list.add_to_tail('a')
# linked_list.add_to_tail('b')
# linked_list.add_to_tail('c')
# print(linked_list._length)
# print(linked_list._tail._value) #c
# print(linked_list._head._value) #a
# print(linked_list._head._next)
# print(linked_list._head._next._value) #b
# print(linked_list._head._next._next._value) #c


# Phase 2 Manual Testing

# # 1. Test whether the list contains_value a value
linked_list = LinkedList()
linked_list.add_to_head('new head node')
# linked_list.add_to_head('new asdf node')
# linked_list.add_to_head('new asdf node')
# linked_list.add_to_head('new asdf node')
# print(linked_list._length)
print(linked_list.contains_value('new head node'))      # True
print(linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
linked_list.insert_value(0, 'hello!')
print(linked_list.get_node(0)._value)                   # `hello!`

print(f'updated: {linked_list._length}')
linked_list.insert_value(3, 'hello-new tail!')
print(linked_list._length)
print(linked_list._tail._value)
linked_list.insert_value(2, 'hello-2')
print(linked_list._length)
print(linked_list._head._next._next._value)

# # 3. Test updating a list node's value at a specific position
linked_list.update_value(0, 'goodbye!')
print(linked_list.get_node(0)._value)                   # `goodbye!`

# # 4. Test removing a node value from the list at a specific position
print(linked_list.get_node(1)._value)                   # `new head node`
print(linked_list.get_node(2)._value)                   # `new head node`
linked_list.remove_node(1)
print(linked_list.get_node(1)._value)                          # None

# # 5. Format the list as a string whenever `print()` is invoked
new_linked_list = LinkedList()
print(new_linked_list)                  # Empty List
new_linked_list.add_to_tail('puppies')
print(new_linked_list)                  # puppies
new_linked_list.add_to_tail('kittens')
print(new_linked_list)                  # puppies, kittens
