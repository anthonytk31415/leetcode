from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque()
        self.right = deque()
        self.length = 0

    def balance(self):          # keep the median at the end of left after each operation
        total_len = len(self.left) + len(self.right) 
        self.length = total_len
        if total_len % 2 == 1: 
            if len(self.left) > len(self.right):
                return 
            else:           
                self.left.append(self.right.popleft())
        if total_len % 2 == 0: 
            if len(self.left) == len(self.right):
                return 
            elif len(self.left) > len(self.right):
                self.right.appendleft(self.left.pop())
            else:
                self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()
        
    def pushMiddle(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)
        self.balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        if self.length == 0: 
            return -1
        res = self.left.popleft()
        self.balance()
        return res

    def popMiddle(self) -> int:
        if self.length == 0: 
            return -1
        res = self.left.pop()
        self.balance()
        return res

    def popBack(self) -> int:
        if self.length == 0: 
            return -1
        if not self.right: 
            res = self.left.pop()
        else: 
            res = self.right.pop()
        self.balance()
        return res


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