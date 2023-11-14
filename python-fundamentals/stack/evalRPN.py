
from collections import deque
def evalRPN(tokens):
    def applyOperation(op, x, y):
        if op == "+": return x + y
        if op == "-": return x - y
        if op == "*": return x * y
        if op == "/": return int(x / y)
    ops = set(["+", "-", "*", "/"])
    tokens = deque(tokens)
    stack = deque([])
    while tokens: 
        cur = tokens.popleft()
        if cur not in ops: cur = int(cur)
        stack.append(cur)
        if stack[-1] in ops: 
            op = stack.pop()
            y = stack.pop()
            x = stack.pop()
            curRes = applyOperation(op, x, y)
            stack.append(curRes)
    return stack.pop()
            
# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# tokens = ["18"]
print(evalRPN(tokens))