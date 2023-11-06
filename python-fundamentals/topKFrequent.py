from heapq import heappop, heappush
from collections import Counter

def topKFrequent(words, k):
    wordCount = Counter(words)
    e = 0
    res = []
    for word in wordCount:
        if e < k: 
            heappush(res,(wordCount[word], word), lambda x,y: (x[0], -x[1]) > (y[0], -y[1]))
            e +=1

        else: 
            cur_count = wordCount[word]
            x0, x1 = res[0]
            print(res, word, cur_count)
            if (cur_count, -word) < x0:
                heappop(res)
                heappush(res,(wordCount[word], word), lambda x,y: (x[0], -x[1]) > (y[0], -y[1]))

    res1 =[]
    print(res)
    for _ in range(k):
        res1.append(heappop(res)[1])
    return res1


# words = ["i","love","leetcode","i","love","coding"]
words = ["i","love","leetcode","i","love","coding"]

# words = ["the","day","is","sunny","the","the","the","sunny","is","is"]

# k = 4
k = 3

print(topKFrequent(words, k))