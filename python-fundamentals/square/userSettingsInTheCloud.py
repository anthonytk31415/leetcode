# start: 203

# convert list of strings into a single string; 

def encode(lst):
    word = '$%$'.join(lst)
    return word


# convert single stirng to list of strings 
def decode(str):
    lst = str.split('$%$')
    return lst
z = (encode(['', 'ab', '', 'gj', '', '32']))
print(z)

print(decode(z))


