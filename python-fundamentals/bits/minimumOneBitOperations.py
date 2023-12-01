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


def minimumOneBitOperations(x):
    bit = [int(y) for y in bin(x)[2:]]
    arr = [0]*len(bit)
    ops = 0
    for i, b in enumerate(bit):
        y = arr[i]
        if b ^ y:
            ops += 2**(len(bit) - i - 1)
            arr[i] = 1
            if i + 1 < len(bit): 
                arr[i+1] = 1

    return ops 



# x = 701001
# x = 750343
x = 173
print(bin(x))
print(minimumOneBitOperations(x))