def longestPalindrome(s):
    if len(s) <= 1: 
        return len(s)

    def calcPalindrome(idx):
        length = 1
        left = idx - 1
        right = idx + 1

        ## extend to right for central equal pieces
        while True: 
            if right < len(s) and s[right] == s[idx]:
                length += 1
                right += 1
            else: 
                break

        # extend left and right
        while True: 
            if right < len(s) and left >= 0 and s[left] == s[right]: 
                length += 2
                right += 1
                left -=1
            else: 
                break
        return left + 1, right - 1

    maxLength = 1
    finalLeft = 0
    finalRight = 0
    for i in range(len(s)):

        left, right = calcPalindrome(i)
        curLength = right - left + 1
        if curLength > maxLength: 
            maxLength = curLength
            finalLeft, finalRight = left, right

    return s[finalLeft: finalRight + 1]



s = 'aabbaabba'

print(longestPalindrome(s))