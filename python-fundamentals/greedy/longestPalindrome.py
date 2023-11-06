# longestPalindrome

def singlechar(word): 
#assume len(word) > 1
    x = word[0]
    return  all([y == x for y in word[1:]])

def longestPalindrome(words):
    # create a hash table to put words in here
    # each time you check if the pair exists in the dictionary
    # if so, 
    # - increment the palindrome counter by length of the string * 2
    # - delete the pair
    pairs = {}
    pairsCounter = 0
    for w in words:
    # keep a dictionary of single character words starting with the letter; 
    # find the longest single character 'word' and keep track of that length e.g. 'eee'
    # then keep track the sum of words with the same character
    # at the end, keep track of the max
        reversed_w = w[::-1]
        if reversed_w in pairs: # check if the pair exists; if so remove it or decrement by 1
            if pairs[reversed_w] >1:
                pairs[reversed_w] -=1
            else: 
                del pairs[reversed_w]
            pairsCounter += len(w)*2
        elif w not in pairs: 
            pairs[w] = 1        # add the w in if 
        else: 
            pairs[w] += 1           # it exists, increment by 1

    max_single = 0
    for x in pairs: 
        if len(x) == 1 and max_single == 0:
            max_single = 1
        elif singlechar(x):
            max_single = max(max_single, len(x))
    
    print(pairs)
    return pairsCounter + max_single

    ## once you go through the words list, you can sort the single char words


x = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]

print(longestPalindrome(x))