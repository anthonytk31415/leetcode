# isValid


# def isValid(s):
#     hash = {}
#     a = set([('{','}'),('(',')'),('[',']')])
#     for char in s:
#         print(char)
#         if char not in hash:
#             if char in ']})' and '[{('[']})'.index(char)] not in hash:
#                 return False
#             hash[char] = 1
#         else:
#             hash[char] +=1
#     def fn (x, hash):
#         if x[0] in hash:
#             if hash[x[0]] == hash[x[1]]:
#                 return True
#         elif x[0] not in hash and x[1] not in hash:
#             return True
#         else:
#             return False
#     z = [fn(x,hash) for x in a]
#     print(z)
#     return all(z)


def isValid(s):
    pair  = {'(':')', ')':'(', '[':']', ']':'[', '{':'}', '}':'{'}
    opens = '({['
    closes = ']})'
    queue = []
    last = ''
    for x in s:
        if x in closes:
            if last != pair[x]:
                return False
            else: 
                queue.pop()
                if (queue):
                    last = queue[len(queue)-1]
                else: 
                    last = ''
        if x in opens:
            last = x
            queue.append(last)
    return len(queue) == 0


x1 = '()[]' # true
x2 = '(())' # true
x3 = ')()(' # false
x4 = '([)]' # false
x5 = '(([[{{]}}]))' #false

# a = set([('{','}'),('(',')'),('[',']')])

# for i in a:
#     print (i[0], i[1])
print(isValid(x1))
print(isValid(x2))
print(isValid(x3))
print(isValid(x4))
print(isValid(x5))
