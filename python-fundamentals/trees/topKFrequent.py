# topKFrequent

# d

## this is slow - lets improve


def topKFrequent(words, k):
    ## put elements into a dictionary with freq[word] = num_occurance
    ## then make a tuple and put them in an array [(freq, word), ...]
    ## then sort the array by freq, then word 

    freq = {}
    for x in words: 
        if x not in freq: 
            freq[x] = 1
        else: 
            freq[x] +=1
    res = []
    for x in freq: 
        res.append((x, freq[x]))
    res = sorted(res, key = lambda x: (-x[1], x[0]))
    return [x[0] for x in res][:k]

# words = ["i","love","leetcode","i","love","coding"]
# print(topKFrequent(words, 2))

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
print(topKFrequent(words, 4))