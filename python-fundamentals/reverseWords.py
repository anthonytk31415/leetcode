s = "Let's take LeetCode contest"

def reverseWords(s):

    
    return ' '.join([x[::-1] for x in s.split(' ')])

print(reverseWords(s))

