# a [bb ]a b [aaaa cc] z 
# 1 2  1 1 4    2  1 


# [aa ]b a b c a [cc] z 
# 2  1 1 1 1 1 2  1

# decisions need to happen when you see consecutives; do you process it now or later? 


# if you have consecutive letters and there are no other adjacent singles, process it immediately
# if you have a single surrounded by single, nothing you can do



# aaa bb aa b cc bb c 
# abbbaaccz

def removeAdjacentChars(char):
    stack = []
    match = False               
    matchChar = None
    for x in char:
        if matchChar == x: 
            continue
        elif not stack: 
            stack.append(x)
        elif stack:             # pop the element, store teh char for future ones
            if stack[-1] == x: 
                match = True
                matchChar = x 
                stack.pop()
            else: 
                stack.append(x)
                match = False
                matchChar = None    
    return ''.join(stack)

# char = 'abbbaaccz'
char = 'aabcaadbbddbc'
print(removeAdjacentChars(char))