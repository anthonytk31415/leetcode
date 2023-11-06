def integerBreak(n):
    res = 1

    for i in range(2, n):
        z = n//i
        r = n % i

        product = z**(i-r) * (z+1)**r
        print(product, z, r, i)
        res = max(res, product)

    return res

dd
print(integerBreak(16))