def minInsertions(s):
    # end = len(s) // 2
    # abcde ; len = 5; do it up to len(5) // 2 but not including
    # abcd; len = 4; do it up to len(4)//2 but not including 
    i = 0
    counter = 0
    while i < len(s):

        if s[i] == s[-1-i]:   
            i +=1
            continue
        else: 
            counter +=1
            if i == 0: 
                s = s + s[0]
            else:
                s = s[:-i] + s[i] + s[-i:]
        print(s)
        i +=1

    return counter
s = 'leetcode'
s = 'mbadm'
s = 'zjveiiwvc'
print(minInsertions(s))

