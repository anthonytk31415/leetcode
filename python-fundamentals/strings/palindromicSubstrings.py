# Palindromic Substrings


def countSubstrings(s):
    count = 0
    if len(s) <= 1: 
        return len(s)

    def pair_helper(s, i, j):
        count2 = 0
        while 0 <= i <= j <= len(s) - 1:
            if s[i] == s[j]:
                count2 +=1
                i -=1
                j +=1
            else: 
                break
        return count2

    for i in range(len(s)):
        count = count + pair_helper(s, i, i) + pair_helper(s, i, i+1)
    return count


print(countSubstrings('aaa'))