# trick here is to implement as a stack and use the open/close brackets to define the compression


# number + open bracket +  stuff + closed bracket
# - if string --> append to current string
# - if number --> build number 
#     - if open bracket --> end number, call function on substring to closed bracket
#         - append answer to string
#     - if series of string, append to 
# - if end of string, return string 

def decodeString(s): 
    stack = []
    chars = ''
    num = ''
    nums = set([str(x) for x in range(0,10)])
    for c in s: 
        if c in nums: 
            if chars: 
                stack.append(chars)
                chars = ''
            num = num + c
        elif c == '[':
            stack.append(num)
            num = ''
            stack.append(c)
        elif c == ']':
            if chars: 
                stack.append(chars)
                chars = ''
            ## pop until you get to bracket, then number, then do string * number
            cMultiply = ''
            key = stack.pop()
            while key != '[':
                cMultiply = key + cMultiply
                key = stack.pop()
            nMultiply = int(stack.pop()) #this is the number
            stack.append(cMultiply * nMultiply)
        else: 
            chars = chars + c
    stack.append(chars)     # append any remaining characters
    return ''.join(stack)

s = '3[a2[c]]'
print(decodeString(s))





# - when bracket is scanned, push the number into stack; when the r
# - load series of numbers into a string, if the next string is not a 


