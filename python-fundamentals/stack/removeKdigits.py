
# Monotonic Stack!
# Pay attention to weird string problems. 

# Time: O(n); Space: O(n)


# k = 3
# 94785818

# 978
# 45818


def removeKdigits(num, k):
    mStack = []
    for n in num: 
        while mStack and mStack[-1] > n and k > 0:
            mStack.pop()
            k -=1
        if not mStack and n == "0": continue
        mStack.append(n) 
    while k > 0 and mStack: 
        mStack.pop()
        k -=1
    if not mStack: return "0"
    return ("").join(mStack)

# print(int(""))

print("1" > "0")

num = "94785818"
k = 3

num = "10200"
k = 1

print(removeKdigits(num, k))