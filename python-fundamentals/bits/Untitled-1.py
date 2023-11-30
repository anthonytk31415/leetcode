

def getMoneyAmount(n):


    def helper(i, j):
        if j - i + 1 <= 1: 
            return 0

        mid = (j - i + 1) // 2
        return mid + helper(mid, j)

    return helper(1, n)