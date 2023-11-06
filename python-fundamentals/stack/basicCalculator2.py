# Basic Calculator II



# if number or + or -: 
# add to stack
# if * or /: 
# stack (operation), 
# x2= next, 
# x1 = stack.pop; 
# then evaluate, 
# then add back to stack 

from collections import deque


def calculate(s):
    
    ## string formatting
    plus_minus = set(['+', '-'])
    multiply_divide = set(['*', '/'])
    s=s.replace(' ', '')                                # no spaces
    s_new = ''
    for x in s: 
        if x in '+-*/':
            s_new += ' ' + x + ' '
        else: 
            s_new +=x 
    s = s_new.split(' ')                                #seperate continuous integers and operations
    s = [int(x) if x.isnumeric() else x for x in s]     # bind integers properly

    stack = deque()
    i = 0

    # handle * and / operations first
    while i < len(s):
        x = s[i]
        if x not in multiply_divide:
            stack.append(x) 
            i +=1
        elif x in multiply_divide: 
            z1 = stack.pop() 
            oper = x
            i +=1
            z2 = s[i]
            if oper == '*':
                stack.append(z1 * z2)
            else: 
                stack.append(int(round(z1 // z2, 0)))
            i+=1

    # handle + and - operations
    while len(stack) > 1:
        z1 = stack.popleft()
        oper = stack.popleft()
        z2 = stack.popleft()
        if oper == '+':
            stack.appendleft(z1 + z2)
        else: 
            stack.appendleft(z1 - z2)
    return stack.pop()




# s = "22 + 3/6 - 9"
s = '1-1+1'
print(calculate(s))


# s = "3+2*2"
# from collections import deque
# def calculate(s):
#     s=s.replace(' ', '')
#     print(s)
#     curNum = ''
#     stack = deque()

#     i = 0
#     # stack numbers and + or -; evalulate * or /
#     while i < len(s):
#         x = s[i]
#         print(x)
#         if x.isnumeric():
#             curNum += x
#             i +=1
#         elif x == '+' or x == '-':
#             if curNum: stack.append(curNum)
#             stack.append(x)
#             curNum = ''
#             i +=1
#         elif x == '*' or x == '/':
#             if curNum: stack.append(curNum)
#             stack.append(x)
#             i +=1
            
#             # get next number, then get to end or get to next operation\
#             # then stack
#             while i < len(s) and s[i].isnumeric():
#                 y = s[i]
#                 curNum +=y
#                 i +=1
#             if curNum: stack.append(curNum)
#             curNum = ''
#             z2 = stack.pop()
#             oper = stack.pop()
#             z1 = stack.pop()
#             if oper == '*':
#                 stack.append(int(round(int(z1) * int(z2),0)))
#             else: 
#                 stack.append(int(round(int(z1) / int(z2),0)))
#     if curNum: 
#         stack.append(curNum)
#         print(curNum)
#     print(stack)
#     while len(stack) >1: 
#         z2 = stack.pop()
#         oper = stack.pop()
#         z1 = stack.pop()
#         print(z1, oper, z2)
#         if oper == '+':
#             stack.append(int(z1) + int(z2))
#         else: 
#             stack.append(int(z1) - int(z2))

#     return stack.pop()

# print(calculate(s))