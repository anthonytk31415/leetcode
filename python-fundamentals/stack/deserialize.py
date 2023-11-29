
# append "[" and integers in to the stack
# - "[" --> append to stack
# - "integer" or "-": add to the current int
# - "," denotes new element and thus the signal to append the cur int to the stack
# - "]" means pop elements from stack until you get to a "[". Then make a list from it. then append to stack 
# - 
from collections import deque

def deserialize(s):

    def convertInt(curInt): 
        stack.append(NestedInteger(int("".join(curInt))))
        curInt = []
        return curInt
    stack, curInt = [], []

    for char in s: 
        if char == "[":
            stack.append(char)
        elif char in set(list("0123456789-")):
            curInt.append(char)
        elif char == ",":
            if curInt: curInt = convertInt(curInt)
        elif char == "]":
            if curInt: curInt = convertInt(curInt)
            curArray = deque()
            while stack[-1] != "[": 
                curArray.appendleft(stack.pop())
            stack.pop()
            curNested = NestedInteger(curArray.popleft())
            while curArray:  
                curNested.add(curArray.popleft())
            stack.append(curNested)                
    if curInt: 
        curInt = convertInt(curInt)
    if type(stack[-1]) == int: 
        return NestedInteger(stack.pop())
    return stack.pop()


class NestedInteger:
    def __init__(self, value):
        self.arr = [value]

    def add(self, elem):
        self.arr.append(elem)

s = "[123,[456,[789]]]"


# s = "324"
d = deserialize(s)
print(d.arr[0].arr)
# print(d.arr[1].arr[1].arr[0])



# print(set(list("0123456789-")))
# print("".join(["a", "b"]))