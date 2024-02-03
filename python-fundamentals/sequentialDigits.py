
# expect at most, n = 9, i = 1


# print(formulate(4, 6))

# conditino of i and n: i + n - 1 < 10

def sequentialDigits(low, high):

    def formulate(n, i):
        res = 0
        for j in range(n):
            res += i
            if j < n-1: res *= 10
            i += 1
        return res

    minDigit, maxDigit = len(str(low)), len(str(high))
    res = []
    for n in range(minDigit, maxDigit + 1):
        for i in range(1, 10):
            if i + n - 1 >= 10: break
            curRes = formulate(n, i)
            if low <= curRes <= high: res.append(curRes)
    return res


low = 1000
high = 999999999
print(sequentialDigits(low, high))