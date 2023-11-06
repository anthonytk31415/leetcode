# backspaceCompare

def backspaceCompare(s, t): 
    i = j = 0
    sNew = tNew = ''
    while i < len(s):
        print(i)
        if s[i] == '#':
            print(sNew)
            if len(sNew)> 0: sNew = sNew[:(len(sNew) - 1)]
        else:
            sNew += s[i]
        i +=1
    while j < len(t):    
        if t[j] == '#':
            if len(tNew) >0: tNew = tNew[:(len(tNew) - 1)]
        else:
            tNew += t[j]
        j +=1
    print(sNew, tNew)
    return sNew == tNew

# print(backspaceCompare('ab#c','abb##c'))

# print(backspaceCompare('b#c','a##bb##c'))




### a stack :

# class Solution:
#     def backspaceCompare(self, S, T):
#         l1 = self.stack(S, [])
#         l2 = self.stack(T, [])
#         return l1 == l2
        
    
#     def stack(self, S, stack):
#         for char in S:
#             if char is not "#":
#                 stack.append(char)
#             else:
#                 if not stack:
#                     continue
#                 stack.pop()
#         return stack


class Solution2:
    def backspaceCompare(s, t):
        a = Solution2.stack(s)
        b = Solution2.stack(t)
        print(a, b)
        return a==b 

    def stack(s):
        stck = []
        for char in s:
            if char == '#':
                if stck:
                    stck.pop()
            else: 
                stck.append(char)
        return stck

print(Solution2.backspaceCompare('b#c','a##bb##c'))