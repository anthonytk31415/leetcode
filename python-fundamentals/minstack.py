from collections import deque

# Trick: stack will keep this tuple: (val, current min)
# O(1) pop/top/getmin
# O(N) storage with tuples (current min for each element)

class MinStack:

    def __init__(self):
        self.stack = deque()        
        # Trick: stack will keep this tuple: (val, current min)
    def push(self, val: int) -> None:
        new_min = val
        if self.stack:         
            last = self.stack.pop()
            if last[1] < val: 
                new_min = last[1]
            self.stack.append(last)
        self.stack.append((val, new_min))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        res = self.stack.pop()
        self.stack.append(res)
        return res[0]

    def getMin(self) -> int:
        if not self.stack: 
            return None
        else: 
            res = self.stack.pop()
            self.stack.append(res)
            return res[1]