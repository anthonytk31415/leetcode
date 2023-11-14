# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150

from collections import deque

# first extract integers, put it all in an array 




def calculate(s):

    def evaluateUpToOpenParen():
        queue = deque([])
        res = 0
        while stack[-1] != "(":
            queue.appendleft(stack.pop())
        stack.pop()
        evaluate(queue)
        stack.append(queue.popleft())

    # all elements should have no parenthesis and can be evaluated 
    def evaluate(queue):
        while len(queue) > 1: 
            if queue[0] == "-":
                queue.popleft()
                num = queue.popleft()
                num = -num
                queue.appendleft(num)
            if len(queue) > 3 and queue[2] == "-": 
                x = queue.popleft()
                ops = queue.popleft()
                queue.popleft()
                y = queue.popleft()
                y = -y
                for element in [y, ops, x]:
                    queue.appendleft(element)
            if len(queue) >= 3:
                x = queue.popleft()
                ops = queue.popleft()
                y = queue.popleft()
                if ops == "+":
                    curRes = x + y
                elif ops == "-":
                    curRes = x - y
                queue.appendleft(curRes)

    def setupActions(s):
        actions = []
        i = 0
        curNum = ""
        while i < len(s):
            char = s[i]
            if s[i] in set(["(",")","+","-", " "]): 
                if curNum: 
                    actions.append(int(curNum))
                    curNum = ""
                if char != " ":
                    actions.append(char)
            else: 
                curNum += char
            i += 1
        if curNum: 
            actions.append(int(curNum))
        return actions


    numbers = set(["1","2","3","4","5","6","7","8","9","0"])

    # if you see a closed bracket, do calcualte cycle until you see an open parens
    # cycle: pop 3 items and do the calcs; if you see 
    actions = setupActions(s) 
    stack = deque([])
    for i, x in enumerate(actions):
        if x == ")": 
            evaluateUpToOpenParen()
        else: 
            stack.append(x)
    # now the stack can be fully evaluated with no parens; all parens are reduced
    evaluate(stack)
    return stack.pop()

    




# a = "1"
# a += "2"
# s = "(1+(4+5+2)-3)+(1986+238) - (-2 + 3)"

s = "-(-3 - 4 - (2 - 3 - (-8 - 8)))"
# print(a)
print(calculate(s))