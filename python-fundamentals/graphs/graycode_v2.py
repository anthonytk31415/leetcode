

# dont forget to convert back to int
def graycode(n):
    memo = {0: ["0"], 1: ["1"]}


    for i in range(2, n + 1):
        left = ["1" + x for x in memo[i-1][::-1]]
        right = ["10" + x[1:] for x in memo[i-1]]
        memo[i] = left + right

    res = []
    for i in range(n+1):
        res = res + [int(x, 2) for x in memo[i]]
    return res





# x = bin(0)
# print(x)
# print(int(x[2:], 2))
# print(type(x))
# print(~x[0])
# # x = x[2:]
# # x << 1
# a = "1"
# a_not = str(int(not int(a)))
# print(a_not)
print(graycode(3))