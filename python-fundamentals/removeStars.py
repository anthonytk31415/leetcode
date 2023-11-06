from collections import deque
def removeStars(s):
    stack = []
    for x in s: 
        if x == '*':
            stack.pop()
        else: 
            stack.append(x)
    return ('').join(stack)

s = "leet**cod*e"
print(removeStars(s))