# len = 5
# abcde  3

from collections import defaultdict

def maxFreq(s, maxLetters, minSize, maxSize): 
    count_words = defaultdict(int)
    cur_count = defaultdict(int)
    max_count = 0
    max_word =''

    for i in range(minSize ):
        cur_count[s[i]] +=1

    if len(cur_count) <= maxLetters:
        count_words[s[:minSize]] +=1
        if max_count < count_words[s[:minSize]]:
            max_count = count_words[s[:minSize]]
            max_word = s[:minSize]
    
    # print(count_words, cur_count)

    for i in range(1, len(s) - minSize + 1):
        # print(s[i:i + minSize])
        first = i
        prev_first = i - 1
        last  = i + minSize - 1

        if cur_count[s[prev_first]] == 1: 
            del cur_count[s[prev_first]]
        else: 
            cur_count[s[prev_first]] -=1

        cur_count[s[last]] +=1

        if len(cur_count) <= maxLetters:
            count_words[s[i:i+ minSize]] +=1

            if max_count < count_words[s[i:i + minSize]]:
                max_count = count_words[s[i:i + minSize]]
                max_word = s[i: i + minSize]

    return max_count

# s = "aababcaab" 
# maxLetters = 2 
# minSize = 3
# maxSize = 4

s = "aaaa"
maxLetters = 1
minSize = 3
maxSize = 3

print(maxFreq(s, maxLetters, minSize, maxSize))