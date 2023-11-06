def numSteps(s):
    num = int(s, 2)
    steps = 0
    while num != 1:
        steps +=1
        print(num)
        if num % 2 == 0: 
            num = int(num // 2)
        else: 
            num = num + 1
    return steps

# s = '1101'
s = "1111011110000011100000110001011011110010111001010111110001"
print(numSteps(s))