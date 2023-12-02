def countNumbersWithUniqueDigits(n):
    memo = {0: 1, 1: 9 }

    if n > 10: return 0
    for i in range(2, n + 1):
        memo[i] = memo[i-1] *(10 - i + 1)

    return sum([memo[i] for i in range(0, n+1)])


print(countNumbersWithUniqueDigits(3))