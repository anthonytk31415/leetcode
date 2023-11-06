# https://leetcode.com/problems/validate-stack-sequences/

from collections import deque

def validateStackSequences(pushed, popped):
    pushed = deque(pushed)
    popped = deque(popped)

    stack = deque()
    while True: 
        if not stack: 
            if not pushed:
                if not popped: 
                    return True
                else: # no pushed, popped is still there
                    return False
            else:     # add front element from pushed into the stack
                stack.append(pushed.popleft())

        elif stack: 
                # first try to pop; if you can't then push; if no more pushed, return false
            if stack[-1] == popped[0]: 
                stack.pop()
                popped.popleft()
            elif not pushed: 
                return False
            elif pushed: 
                stack.append(pushed.popleft())

# pushed = [1,2,3,4,5]
# popped = [4,5,3,2,1]

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(validateStackSequences(pushed, popped))