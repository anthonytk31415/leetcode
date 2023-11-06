# tuples

# properties
# immutable; cannot append
# iterable 


odd = (1,3,5,7,9)
even = (2,4,6,8)

aTuple = ('d','a','b','e','z','t','h')

#can sort a tuple using sorted (not sort b/c tuples are immutable) i.e. make a NEW tuple that's sorted
aTupleSorted = tuple(sorted(aTuple))
print(aTupleSorted)

scores = (15, 66, 34, 99, 29)
print(scores)
print(max(scores))
print(min(scores))
print(sorted(scores))

# ex of list comprehension
someList = [1,2,3]
[x for x in someList if x < 5]

# sort an array of tuples based on the second value
# the "key" is a function that provides the value 
def index_sort(list_t):
    return sorted(list_t, key= lambda x: x[1])