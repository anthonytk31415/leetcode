class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.head = Node()         #this will always point at the front
        self.counter = 0
        self.tail = Node()         # this prev will always point at the tail
        self.head.next, self.tail.prev = self.tail, self.head
        self.mid = None

    def pushFront(self, val: int) -> None:
        # create node, attach to newFront: next, prev
        newFront = Node(val)
        newFront.next = self.head.next
        newFront.prev = self.head
        
        self.head.next.prev = newFront      # assign 2nd's prev to newFront
        self.head.next = newFront           # assign to head the next

        if self.counter == 0: 
            self.mid = self.head.next

        elif self.counter %2 == 1: 
            self.mid = self.mid.prev

        self.counter +=1

        # print('val and mid: ', val, self.mid)

    def pushMiddle(self, val: int) -> None:
        newMid = Node(val)
        if self.counter == 0: 
            self.head.next = newMid
            newMid.prev = self.head
            self.tail.prev = newMid
            newMid.next = self.tail

        elif self.counter %2 == 1:            # odd >> insert "mid" element to left of current mid 
            self.mid.prev.next = newMid
            newMid.prev = self.mid.prev
            newMid.next = self.mid
            self.mid.prev = newMid
        elif self.counter % 2 == 0:
            self.mid.next.prev = newMid
            newMid.next = self.mid.next
            newMid.prev = self.mid
            self.mid.next = newMid  
        self.mid = newMid
        self.counter +=1

    def pushBack(self, val: int) -> None:
        newBack = Node(val)
        newBack.prev = self.tail.prev
        newBack.next = self.tail

        self.tail.prev.next = newBack
        self.tail.prev = newBack

        if self.counter == 0: 
            self.mid = self.tail.prev

        elif self.counter %2 == 0: 
            self.mid = self.mid.next

        self.counter +=1

    def popFront(self) -> int:
        if self.counter == 0: 
            return -1
        front = self.head.next.val
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

        if self.counter == 1: 
            self.mid = self.head.next
        elif self.counter %2 == 0:
            self.mid = self.mid.next

        self.counter -=1
        return front

    def popMiddle(self) -> int:
        if self.mid: 
            mid = self.mid.val
        if self.counter == 0: 
            return -1
        
        elif self.counter % 2 == 1: 
            self.mid.prev.next, self.mid.next.prev = self.mid.next, self.mid.prev
            self.mid = self.mid.prev
        elif self.counter % 2 == 0: 
            self.mid.prev.next, self.mid.next.prev = self.mid.next, self.mid.prev
            self.mid = self.mid.next
        self.counter -=1
        return mid

    def popBack(self) -> int:
        # print(self.counter)
        if self.counter == 0: 
            return -1

        back = self.tail.prev.val

        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

        if self.counter == 1: 
            self.mid = None
        elif self.counter %2 == 1:
            self.mid = self.mid.prev 

        self.counter -=1
        return back

    def print(self):
        node = self.head
        while node: 
            if self.mid: 
                print(node.val, self.mid.val)
            else: print(node.val)
            node = node.next

    def printBack(self):
        node = self.tail
        while node: 
            if self.mid: 
                print(node.val, self.mid.val)
            else: print(node.val)
            node = node.prev



queue = FrontMiddleBackQueue()

# ["FrontMiddleBackQueue","pushFront","pushFront","pushFront","pushFront","popBack","popBack","popBack","popBack"]
# [[],[1],[2],[3],[4],[],[],[],[]]

queue.popMiddle()
queue.popMiddle()
queue.popMiddle()
queue.pushMiddle(5)
queue.popBack()
queue.popFront()
queue.popMiddle()

# queue.pushFront(1)
# queue.pushFront(2)
# queue.pushFront(3)
# queue.pushFront(4)
# queue.popBack()
# queue.popBack()
# queue.popBack()
# queue.popBack()
# queue.pushFront(2)
# queue.pushFront(1)
# queue.pushFront(0)
# queue.pushBack(7)
# queue.pushBack(8)
# queue.pushBack(9)
# queue.pushMiddle(5)
# queue.pushMiddle(4)
# queue.popBack()
# queue.popFront()

# # queue.popBack()
# # queue.popFront()
# # queue.popBack()
# # queue.popFront()
# queue.print()
queue.printBack()

# print(queue.tail.prev.val)
