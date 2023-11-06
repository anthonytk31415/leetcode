from collections import Counter
def countBits(n):
    bin_n = bin(n)
    bin_n = bin_n[2:]
    bin_counter = Counter(bin_n)
    return bin_counter['1']

print(countBits(2))