from collections import Counter, defaultdict
# hash table with while loops. 

# since there are 26 chars, the worst case scenario is that you have chars 
# that have freq >= 26 and they all need to be lined up at 0, 1, ... , 25 or so. 
# so you're really capped at O(n) Time to get the frequency of the counter
# and then for each char (only 26 of them) you do the while loop 26 times max 
# to push that count down to its own spot. 

# space: O(1) for 26 chars frequency


def minDeletions(s):

    counts = Counter(s)
    freqs = defaultdict(list)
    for x in counts: 
        freqs[counts[x]].append(x)
    
    freqKeys = list(freqs.keys())
    freqKeys.sort(key = lambda x: -x)
    res = 0
    for x in freqKeys: 
        while len(freqs[x]) > 1: 

            curFreq = x
            curChar = freqs[x].pop()
            while curFreq > 0 and curFreq in freqs: 
                curFreq -=1
                res += 1
            freqs[curFreq].append(curChar)
    return res

s = "aaaaabbbbbcccccddddv"
print(minDeletions(s))

