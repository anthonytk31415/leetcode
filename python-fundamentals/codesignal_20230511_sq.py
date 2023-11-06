print('hello world')


## palindrome


def isPalindrome(s):
    if len(s) <= 1: 
        return True
    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else: 
        return False

def solution(s):
    if len(s) <= 1: 
        return s
    prefixes = []
    max_s = ''
    max_len_s = 0
    max_s_idx = -1
    for i in range(len(s)):
        cur_s = s[:i+1]

        if isPalindrome(cur_s): 
            prefixes.append(cur_s)
            if len(cur_s) > max_len_s:
                max_s = cur_s
                max_len_s = len(cur_s)
                max_s_idx = i
    
    if max_len_s >= 2: 
        s = s[max_s_idx +1 :]
        return solution(s)
    else: 
        return s
        

s = 'codesignal'
s = 'babesselxv'

# s = 'aaacodedoc'

# a = 'anthony'

# print(isPalindrome(a))
# print(isPalindrome('aabbaa'))
# print(isPalindrome('aabaa'))
# i = len('anthony') - 1
# print(a[i+1:])

print(solution(s))