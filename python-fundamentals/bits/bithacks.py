

x = 3
y = 14
r = x ^ ((x ^ y) & -(x < y))


# On some rare machines where branching is very expensive and no condition move instructions exist, 
# the above expression might be faster than the obvious approach, r = (x < y) ? x : y, even though it 
# involves two more instructions. (Typically, the obvious approach is best, though.) 


# It works because if x < y, then -(x < y) will be all ones, so r = y ^ (x ^ y) & ~0 = y ^ x ^ y = x. Otherwise, if x >= y, then -(x < y) will be all zeros, so r = y ^ ((x ^ y) & 0) = y. On some machines, evaluating (x < y) as 0 or 1 requires a branch instruction, so there may be no advantage.
# To find the maximum, use:
print(r)

r = y ^ ((x ^ y) & -(x < y)); # min(x, y)


r = x ^ ((x ^ y) & -(x < y)); # max(x, y)


# f even?
v = 93
f = (v & (v - 1)) == 0
print(f)