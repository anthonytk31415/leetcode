# combination practice


# combinations: n choose k, order does not matter
# using itertools: 
from itertools import combinations, permutations

a = [1,2,3,4]
comb = list(combinations(a, 3))
print(comb)

## to program n choose k: 
## 2 accomodates for 2 more slots after i taking the first slot for k=3 total  slots
res = []
for i in range(len(a)-2):
    for j in range(i+1, len(a) - 1):
        for k in range(j+1, len(a)):
            res.append((a[i], a[j], a[k]))
print(res)



perm = list(permutations(a, 3))
print(perm)


res = []
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if i != j and i !=k and j !=k:
                res.append((a[i], a[j], a[k]))
print(res)
