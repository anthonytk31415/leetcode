def fill_tuple(x, value, length):
    mylist = list(x)
    list_output = []
    for tup in mylist:
        lst = list(tup)
        while len(lst) < length:
            lst.append(value)
        list_output.append(tuple(lst))
    return tuple(list_output)

print(fill_tuple(((58, 1, 5), (0, 3), (45, ), (24, 23)), 2, 3))    #> ((58, 1, 5), (0, 3, 2), (45, 2, 2), (24, 23, 2))
print(fill_tuple(((1, ), (5, 7), (55, 22), (80, 52, 20)), 5, 4)) 


