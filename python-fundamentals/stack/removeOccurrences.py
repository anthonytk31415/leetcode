from collections import deque
def removeOccurrences(s, part):

    testing = True
    while testing: 
        testing = False
        idx = s.find(part)
        if idx > -1: 
            testing= True
            s = s[:idx] + s[(idx + len(part)):]
            # print(s, idx)
    return s


s = "daabcbaabcbc"
part = "abc"




s = "axxxxyyyyb"
part = "xy"


s = "gjzgbpggjzgbpgsvpwdk"
part = "gjzgbpg"
blah = '123'
print(s.find(blah))

# s = "gjzgbpgsvpwdk"
print(removeOccurrences(s, part))