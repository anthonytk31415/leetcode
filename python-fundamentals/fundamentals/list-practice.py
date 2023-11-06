# lists

mylist = ['a','b','d','abba','jimmy','James','lebron']

# sort performed on the list itself
mylist.sort(key=str.lower)

print(mylist)
mylist2 = ['a','b','d','abba','jimmy','James','lebron']

mylist3 = sorted(mylist2)

# returns a new list
mylist4 = sorted(mylist2, key=str.lower)
print(mylist2)
print(mylist3)
print(mylist4)

a = [1,2,3]
print(sum(a))


a.insert(0,0)
print(a)