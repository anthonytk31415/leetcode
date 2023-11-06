# substring matching



## naive approach

# string a from i = 0 to i = n-1; length = n
# s = "delta" moves from i to 0 : n - 1 - m

# string to match 0>m-1; length = m



# 0        
# 0123456789
# abcabaabca
#    abaa
#    0..m-1    

a = 'anthony'
b = 'hozn'


# naive approach
# if match, return position of string where the match begins, else return false
# Time: O(N^2), running through each letter in string a and checking for each letter in the substring
# Space: O(1)
def findMatch(a, b):
    for i in range(len(a)-len(b)):
        breakCond = False
        for j in range(len(b)):
            if b[j] != a[i+j]:
                breakCond = True
                break
        if breakCond == False: ## all strings were checked and didn't trigger break cond 
            return i
    return False

# a bit smoother design
def findMatch2(a, b):
    for i in range(len(a)-len(b)):
        if b == a[i:i+len(b)]:
            return True
    return False

print(findMatch2(a, b))
