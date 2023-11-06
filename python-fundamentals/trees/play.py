class Stefan:
    def fn1(x):
        return Stefan.fn2(x) + 3

    def fn2(y):
        return y + 1

print(Stefan.fn1(3))