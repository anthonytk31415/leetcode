# class Node: 
#     def __init__(self, val=None):
#         self.val = val; 
#         self.next = None; 
#         self.prev = None
    

# class MyCircularDeque:

#     def __init__(self, k: int):
#         self.head = Node()
#         self.tail = Node()
#         self.countNodes = 0
#         self.maxNode = k
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def insertFront(self, value: int) -> bool:
#         if self.isFull(): return False
#         node = Node(value)
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node
#         node.prev = self.head
#         self.countNodes += 1
#         return True


#     def insertLast(self, value: int) -> bool:
#         if self.isFull(): return False
#         node = Node(value)
#         self.tail.prev.next = node
#         node.prev = self.tail.prev 
#         node.next = self.tail 
#         self.tail.prev = node 
#         self.countNodes += 1
#         return True
        
#     def deleteFront(self) -> bool:
#         if self.isEmpty(): return False
#         nodeAfter = self.head.next.next
#         nodeAfter.prev = self.head
#         self.head.next = nodeAfter
#         self.countNodes -= 1        
#         return True


#     def deleteLast(self) -> bool:
#         if self.isEmpty(): return False
#         nodeBefore = self.tail.prev.prev
#         nodeBefore.next = self.tail
#         self.tail.prev = nodeBefore
#         self.countNodes -= 1        
#         return True  

#     def getFront(self) -> int:
#         if self.isEmpty(): return -1
#         return self.head.next

#     def getRear(self) -> int:
#         if self.isEmpty(): return -1
#         return self.tail.prev

#     def isEmpty(self) -> bool:
#         return self.countNodes == 0

#     def isFull(self) -> bool:
#         return self.countNodes == self.maxNode


################################################################################

from collections import deque 

class MyCircularDeque:

    def __init__(self, k: int):
        self.maxNode = k
        self.deque = deque(); 

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.deque.appendleft(value)
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.deque.append(value)
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.deque.popleft()
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.deque.pop()
        return True  

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.maxNode





# # Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)

param_1 = obj.insertFront(4)
param_2 = obj.insertLast(10)

# print(obj.head.next.next.next.val)
# print(obj.tail.prev.prev.val)

param_3 = obj.deleteFront()

param_4 = obj.deleteLast()
# print(obj.head.next.val)
# print(obj.tail.prev.val)
# print(obj.getFront())
param_6 = obj.getRear()
print(param_6)
param_7 = obj.isEmpty()
print(param_7)
print(obj.isFull())

obj.insertFront(1)
obj.insertFront(2)
obj.insertFront(3)
print(obj.insertFront(3))