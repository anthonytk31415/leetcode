# Time: O(high)
# Space: O(high)

def countGoodStrings(low, high, zero, one):

    count = 0
    memo = {}
    ## we assume cur will always be less than high
    ## we approach this with a dfs
    memo[0] = 1
    check = [zero, one]
    # print(check)
    for i in range(1, high + 1):
        cur_res = 0
        for x in [zero, one]:
            # print('x:', x)
            if x <= i: 
                cur_res += memo[i - x]
                # print('x:', x,'i:',  i, 'memo[i-x]:', memo[i-x], 'cur_res:', cur_res)

        memo[i] = cur_res
        if low <= i <= high: 
            count += cur_res

    # print(memo)
    return count  % (10 ** 9 + 7)

# this is too slow; 
# how can we somehow memoize the results?
# 


# low = 2
# high = 3
# zero = 1
# one = 2
## 5

# low = 3
# high = 3
# zero = 1
# one = 1


# low = 2
# high = 3
# zero = 1
# one = 1


low = 200
high = 200
zero = 10
one = 1

print(countGoodStrings(low, high, zero, one))