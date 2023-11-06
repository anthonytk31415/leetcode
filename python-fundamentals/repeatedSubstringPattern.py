def repeatedSubstringPattern(s):
    for i in range(len(s)//2):
        cur = s[:i+1]
        if s == cur *( len(s) // len(cur)):
            return True
    return False


s = "abcabcabcabc"

print(repeatedSubstringPattern(s))
