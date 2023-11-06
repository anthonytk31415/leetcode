# Python: Implement a deque by using three stacks. The queue should provide:
# size(), isEmpty(), offerFirst(), offerLast(), pollFirst(), pollLast(), peekFirst() and peekLast() operations. When the queue is empty, pollFirst(), pollLast(), peekFirst() and peek() should return None

from collections import deque

class myDeque: 
    def __init__(self):
        self.size = 0
        self.len_left = 0
        self.len_right = 0
        self.intermediate = 0
        self.left = deque()
        self.right = deque()
        self.intermediate = deque()
    
    def setSizes(self):
        self.size = len(self.left) + len(self.right)
        self.len_left = len(self.left)
        self.len_right = len(self.right)
        
    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def offerFirst(self, val):
        self.left.append(val)
        self.setSizes()

    def offerLast(self, val):
        self.right.append(val)
        self.setSizes()

    def pollFirst(self):
        if self.size == 0: 
            res = None
        else: 
            if self.len_left > 0: 
                res = self.left.pop()
            else:           # use the intermediate: take the right, push/pop n/2 elements to the intermediate, , push/pop rest of elements from right to left, then pushpop all intermidate
                            # to right, then do pop on left
                for _ in range(self.len_right//2):
                    self.intermediate.append(self.right.pop())
                
                while self.right:
                    self.left.append(self.right.pop())
                while self.intermediate:
                    self.right.append(self.intermediate.pop())
                res = self.left.pop()
        self.setSizes()
        return res

    def pollLast(self):
        if self.size == 0: 
            res = None
        else: 
            if self.len_right > 0: 
                res = self.right.pop()
            else:           # use the intermediate: take the right, push/pop n/2 elements to the intermediate, , push/pop rest of elements from right to left, then pushpop all intermidate
                            # to right, then do pop on left
                for _ in range(self.len_left//2):
                    self.intermediate.append(self.left.pop())
                while self.left:
                    self.right.append(self.left.pop())
                while self.intermediate:
                    self.left.append(self.intermediate.pop())
                res = self.right.pop()
        self.setSizes()
        return res

    def peekFirst(self):
        if self.size == 0: 
            res = None
        res = self.pollFirst()
        self.left.append(res)
        self.setSizes()
        return res

    def peekLast(self):
        if self.size == 0: 
            res = None
        res = self.pollLast()
        self.right.append(res)
        self.setSizes()
        return res

q = myDeque()
q.offerFirst(3)
q.offerFirst(2)
q.offerFirst(1)
q.offerLast(88)
q.offerLast(89)
q.offerLast(90)
print(q.left, q.right)


# print(q.pollFirst())
# print(q.pollFirst())
# print(q.pollFirst())
# print(q.left, q.right)
# print(q.pollFirst())
# print(q.pollFirst())
# print(q.pollFirst())
# print(q.pollFirst())

print(q.pollLast())
print(q.pollLast())
print(q.pollLast())



print('marker', q.left, q.right)

print(q.peekFirst())
print(q.peekLast())
print('marker', q.left, q.right)

print(q.pollLast())
print(q.pollLast())
print(q.pollLast())
print(q.pollLast())
print(q.peekFirst())
print(q.peekLast())
# pollLast()     
# peekFirst()
# peekLast()