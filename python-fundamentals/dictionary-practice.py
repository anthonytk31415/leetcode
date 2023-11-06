#dictionaries



keys = ['a','b','c']
values = [1,2,3]

#"zip them up" 
mydict = dict(zip(keys, values))
print(mydict)

myset = set(zip(keys, values))
print(myset)



# iterable mydict listlike objects: keys = key, values = iterable values, items = key value pairs
for i in mydict.keys():
    print(i)

for j in mydict.values():
    print(j)

for k in mydict.items():
    print(k)
