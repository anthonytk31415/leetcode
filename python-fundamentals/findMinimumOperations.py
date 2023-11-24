def findMinimumOperations(s1, s2, s3):
    operations = 0
    minLength = min(len(s1), len(s2), len(s3))
    s1 = [x for x in s1] 
    s2 = [x for x in s2] 
    s3 = [x for x in s3] 

    for x in [s1, s2, s3]:
        while len(x) > minLength:
            operations += 1
            x.pop()        

    if s1 == s2 == s3: 
        return operations

    if s1[:1] != s2[:1] or s2[:1] != s3[:1]:
        return -1

    # stop when the i's are not equal
    i = 1
    while i < minLength:
        if not (s1[i] == s2[i] == s3[i]):
            break 
        i += 1

    return operations + (minLength - i) * 3

s1 = 'aaaabcaa'
s2 = 'aaaace'
s3 = 'aaaabc'



# s1 = "abc"
# s2 = "abb"
# s3 = "ab"

s1 = 'a'
s2 = 'a'
s3 = 'a'
print(findMinimumOperations(s1, s2, s3))