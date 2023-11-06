# Palindrome Partitioning

from collections import deque
def partition(s):
    arr = [x for x in s]
    res = set()
    q = deque()
    res.add(tuple(arr))
    q.append(arr)
    while q: 
        cur = q.popleft()
        for i in range(len(cur)):
            ## check for neighbors
            if 0 <= i-1 <= len(cur)-1 and 0 <= i +1 <= len(cur) - 1: 
                if ((len(cur[i-1]) == 1 and cur[i-1] == cur[i+1]) or     # equal for singular string
                    (len(cur[i-1]) > 1 and cur[i-1] == cur[i+1][::-1])):  # neighbor == reversed
                    new_cand = cur[:i-1] + [cur[i-1]+cur[i]+cur[i+1]] + cur[i+2:]
                    if tuple(new_cand) not in res: 
                        res.add(tuple(new_cand))
                        q.append(new_cand)
            # check for equal pairs
            if i+1 <= len(cur)-1:
                if (cur[i] == cur[i+1]):  
                    new_cand = cur[:i] + [cur[i] + cur[i+1]] + cur[i+2:]
                    if tuple(new_cand) not in res: 
                        res.add(tuple(new_cand))
                        q.append(new_cand)
    return [list(x) for x in res]

print(partition('aaabaaa'))

# aaabbb

# a a a b a a a 

# # pairs from first, then neighbors
# aa a b a a a 
# a aa b a a a 
# a a a b aa a
# a a a b a aa 
# aaa b a a a 
# a aba a a a 
# a a a b aaa 

# # 
# ## check if (1) equal or (2) if len > 1 and (a) = reverse(b)



# aaa b b b
# a a a bbb 

# aa 