def dummy(x):
    count = [0]
    def helper(y):
        count[0] += y
        return 
    
    helper(x)
    print(count)
    return count[0]

print(dummy(2))

