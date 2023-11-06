
# Time: O(n)
# space: O(1)

def countBinarySubstrings(s):
    counter = 0
    starting = s[0]

    count_zero, count_one = 0, 0
    alternates = 0

    for i in range(0, len(s)):
        if s[i] != starting: 
            alternates +=1
            starting = s[i]
        if alternates == 2: 

            counter += min(count_zero, count_one)
            if starting == '0': 
                count_zero = 0
            else: 

                count_one = 0
            alternates = 1
        if s[i] == '0':
            count_zero +=1
        else: 
            count_one +=1

        # print(i, count_zero, count_one, starting, alternates)
    if count_zero > 0 and count_one > 0: 
        counter += min(count_zero, count_one)

    return counter


s = "00110011"
# s = "10101"
print(countBinarySubstrings(s))