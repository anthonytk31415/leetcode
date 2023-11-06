# O(N) time; space: O(1)

# initially, each number can be visited once; then for each number, the next number in the sequence
# can be built by adding its knight paths from the last step recursively. 


def knightDialer(n):
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n0 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    i = 1
    while i < n: 
        n5 = 0
        n1, n2, n3, n4, n6, n7, n8, n9 , n0= n8 + n6, n7 + n9,  n4 + n8,  n3 + n9 + n0, n1 + n0 + n7, n2 + n6 , n1 + n3 , n2 + n4 ,  n4 + n6 
        i += 1
    return (n1 +  n2 +  n3 +  n4 +  n5 +  n6 +  n7 +  n8 +  n9 +  n0) % (10**9 + 7)

print(knightDialer(3131))