def minimumOneBitOperations1(x):
    def changeLastBit(x):
        x_lastBit = x & 1
        bitWise_x_lastBit = ~x_lastBit & 1
        return ((x >> 1)<< 1) | bitWise_x_lastBit

    # returns position of the first 1 from right to left of a bit representation
    # this is an O(n) operation; can I reduce this to O(1)?

    # In this update, we use x & -x
    # note -x is the same as ~x + 1. Think of this as a definition and it's called two's complement. 
    # in this form, if we do x & -x, we get the first occurrence of 1. 
    def findFirstOne(x):
        # count = 0
        # n = 1
        # while x & (n << count) == 0: 
        #     count += 1
        # return count + 1
        return (x & -x ).bit_length()

    # take x, shift to 1 more than first one position, change last bit, shift left one 
    def changePastFirstOne(x):
        firstOnePosition = findFirstOne(x)    
        bitAfterFirst = (changeLastBit(x >> firstOnePosition) << 1 | 1) << firstOnePosition - 1
        return bitAfterFirst
    
    z = 0
    changeLast = True
    numOperations = 0
    while z != x: 
        if changeLast: 
            z = changeLastBit(z)
        else: 
            z = changePastFirstOne(z)
        
        changeLast = not changeLast
        numOperations += 1
    return numOperations



# even this is too slow; maybe can do this is constant time; this iseems like a linear operation that needs to now get faster...
# this is in O(length of bit of x)
# this was a mother fucking marathon. 


# Intuition: write out starting from 0 to some integer. 
# Notice that you alternate between operation 1 and operation. They're irreversible. There's only one way to go. 
# Start at 0 and work towards the 0th digit (rightmost). Concept is we'll do the min operations to get to the largest signficant number, and
# subsequently add more operations to get to the full n digit number. 
# So iterate across your binary x. 
# Say your binary x = 10000 (length = 5). To get to a 5 digit number, the min operation is x^(L-1) and we get to 11000. 
# Call y our binary that starts with 0 and works towards x.
# For each i, if binary[i] ^ binary[y] then add 2**(len(bit) - i - 1) to the operations and update y[i]


def minimumOneBitOperations(x):
    bit = [int(y) for y in bin(x)[2:]]
    arr = [0]*len(bit)
    ops = 0
    print(arr)
    for i, b in enumerate(bit):
        y = arr[i]
        if b ^ y:
            ops += 2**(len(bit) - i - 1)
            arr[i] = b
            if i + 1 < len(bit): 
                arr[i+1] = 1
        print(arr)
    return ops 

# I should spend time figuring out how this is done: 
def minimumOneBitOperations2(n):
    res = 0
    print(bin(n))
    while n:
        res = -res - (n ^ (n - 1))
        n &= n - 1
        print(bin(n))
    return abs(res)

# x = 701001
# x = 750343
x = 173
print(bin(x))
print(minimumOneBitOperations2(x))