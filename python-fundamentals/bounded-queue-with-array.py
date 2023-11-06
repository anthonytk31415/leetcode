# queue 

# 0,1,2,3,4


class boundedQueue:
    def __init__(self, n):
        self.capacity = n
        self.queue = [None]*n
        self.front =0 
        self.back = 0
        self.size = 0

    # pointer of back will always be the first empty slot after the end
    # pointer of front will be at the front element
    # when it's empty, f = b

    # when pushing, increase back up one
    def push(self, val): 
        if self.size == self.capacity: 
            return False
        self.queue[self.back] = val
        if self.back== self.capacity - 1: # go from back to front
            self.back = 0
        else: self.back +=1          
        self.size +=1
    
    def pop(self):
        if self.isEmpty(): 
            return False
        res = self.queue[self.front]
        self.queue[self.front] = None
        ## push the front + 1 or around 
        if self.front == self.capacity - 1: 
            self.front = 0
        else: self.front +=1

        self.size -=1
        return res

    def peek(self):
        if self.size > 0: 
            return self.queue[self.front]
        else: 
            return False

    def isEmpty(self):
        return self.size == 0


q = boundedQueue(4)

q.push(0)
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
print(q.pop())
print(q.pop())
print('1 - current queue: ', q.queue)
q.push(5)
q.push(6)
q.push(7)
print(q.pop())
print(q.pop())
print(q.queue)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())