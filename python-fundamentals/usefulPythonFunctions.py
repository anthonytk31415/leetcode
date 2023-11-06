# enumerate
# alist = ['a','b','c']
# enumerate returns an interable with tuples (0,'a'), (1, 'b'), (2, 'c'), ...

# sorted: 
# for sorting; two specify a key, define a function that returns the key
# if two keys, define a lambda function with the key command;
#  you can control desceding, and ascending behavior; default is ascending
sorted(thelist, key = lambda x: (x[0], x[1]))



# array slicing
# https://stackoverflow.com/questions/509211/understanding-slicing
a[low:high:step] is the array from low to high, noninclusive of high with increments of step

if step is negative:
a[high:low:step] is the array from high to low, noninclusive of low, with increments of