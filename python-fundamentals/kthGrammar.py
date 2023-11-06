def kthGrammar(n,k):

    memo = {'0': '01',
             '1': '10'}

    def divide_conquer(x, memo):
        if x in memo: 
            return memo[x]
        else: 
            q = len(x)//2
            res = divide_conquer(x[:q], memo) + divide_conquer(x[q:], memo)
            memo[x] = res
            return res

    res = '0'
    if n == 1: 
        return int(res[k-1])
    for _ in range(2, n+1):
        res = divide_conquer(res, memo)

    # print('final res:', res)
    return str(res[k-1])

print(kthGrammar(30,434991989))

# here's the solution with bit manipulation; should i learn? 

def kthGrammar(n,k):
    return bin(k - 1).count('1') & 1

# x = '0110'
# print('x')
# q = len(x)//2
# print(x[:q])
# print(x[q:])