from collections import deque

# class MyQueue:

#     def __init__(self):
#         self.pushing = deque()
#         self.popping = deque()

#     def push(self, x: int) -> None:

#         while self.popping:
#             self.pushing.append(self.popping.pop()) 
#         self.pushing.append(x)

#     def pop(self) -> int:
#         if self.empty():
#             return None
#         while self.pushing:
#             self.popping.append(self.pushing.pop())
#         return self.popping.pop()

#     def peek(self) -> int:
#         res = self.pop()
#         self.pushing.append(res)
#         while self.popping:
#             self.pushing.append(self.popping.pop())
#         return res

#     def empty(self) -> bool:
#         return (not self.pushing) and (not self.popping)

# Trick: 
# - take two stacks, q_push and q_pop
# - invariant: if q_pop is filled, popping q_pop will always return the earliest element
# - peek will move via popping elements from q_push into q_pop to maintain the variant when pop is not filled
# - can use peek to move stuff so that when pop is called, q_pop is guaranteed to be filled

# O(1) amortized time; space: O(N) to maintain the N elements


class MyQueue:

    def __init__(self):
        self.q_push = deque()
        self.q_pop = deque()

    def push(self, x: int) -> None:
        self.q_push.append(x)

    def pop(self) -> int:
        self.peek()
        return self.q_pop.pop()

    def peek(self) -> int:
        if not self.q_pop: 
            while self.q_push:
                self.q_pop.append(self.q_push.pop())
        res = self.q_pop.pop()
        self.q_pop.append(res)
        return res
    
    def empty(self) -> bool:
        return (not self.q_push) and (not self.q_pop)



x = MyQueue()
# print(x.empty())
x.push(1)
# print(x.empty())
x.push(2)
print(x.peek())
print(x.pop())
print(x.empty())


