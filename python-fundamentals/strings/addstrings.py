# addstrings


def addStrings(num1, num2):

    res = ''
    carry = 0
    while num1 and num2: 
        s1 = int(num1[-1])
        num1 = num1[:-1]
        s2 = int(num2[-1])
        num2 = num2[:-1]
        x = str((s1 + s2 + carry) % 10)
        res = x + res
        if s1 + s2 + carry > 9: 
            carry = 1
        else:
            carry = 0    
    while num1: 
        s1 = int(num1[-1])
        num1 = num1[:-1]
        s2 = 0
        x = str((s1 + s2 + carry) % 10)
        res = x + res
        if s1 + s2 + carry > 9: 
            carry = 1
        else:
            carry = 0    
    while num2:
        s1 = 0
        s2 = int(num2[-1])
        num2 = num2[:-1]
        x = str((s1 + s2 + carry) % 10)
        res = x + res
        if s1 + s2 + carry > 9: 
            carry = 1
        else:
            carry = 0
    if carry: 
        res = str(carry) + res
    
    return res

print(addStrings('12399', '299993'))