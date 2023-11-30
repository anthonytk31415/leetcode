


num = 10
num_b2 = bin(num)[2:]
print(num_b2)

rightmost_num = num & 1

print(bin(~rightmost_num & 1))