# Longest Repeating Character Replacement

# Time: O(n)
# space: O(n)

#### The Idea ####
# use left and right pointers
# iterate cross all n for right pointer
# at each step, keep track of your occurances of each char in your current L-R string
# evaluate max_length at every step 
# key condition: 
# if current_length - max(individual char occurance) <= k (which means you use have enough "k's" to replace to add to the max individual char occurance)
# --> max_length = current_length
# if not, then you have too many nonmax chars so slide your left pointer +=1 and remove the char frequency from your frequency table

def characterReplacement(s, k):
    c_freq = {}
    max_length = 0
    l = 0

    for r in range(len(s)):
        if s[r] not in c_freq:
            c_freq[s[r]] = 0
        c_freq[s[r]] +=1

        cur_len = r - l + 1
        if cur_len - max(c_freq.values()) <= k: 
            max_length = cur_len
        else:
            c_freq[s[l]] -=1    
            l +=1

    return max_length

print(characterReplacement('aabadeaa', 1))