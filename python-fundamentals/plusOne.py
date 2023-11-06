# def plusOne (digits):
#     num = 0
#     for i in range(len(digits)):
#         exp = len(digits)- i - 1
#         num = num + 10 ** exp * digits[i]
#     return [int(x) for x in str(num + 1)]
    

def plusOne (digits):
    num = ''
    for d in digits:
        num += str(d)
    return [int(x) for x in str(int(num) + 1)]
    



# len = 4
# 0,1,2,3
# 3, 2, 1, 0

x1 = [1,9,9,9]
x2 = [9,9]
x3 = [1,3,2,1]
print(plusOne(x1))
print(plusOne(x2))
print(plusOne(x3))