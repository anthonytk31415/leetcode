# isSubsequence
# O(n) running time (because you search the index up to t times, but never more than t because your input t decreases with every search)
# O(1) storage via iter t and some indeces

def isSubsequence(s, t):
    t_iter = t
    for char in s:
        try: 
            index = t_iter.index(char)
            t_iter = t_iter[index+1:]
            # print(f'truth :{char}, {t_iter}')
        except: 
            return False
    return True

print(isSubsequence('ya', 'anthony')) # false
print(isSubsequence('ant', 'anthony')) # true
print(isSubsequence('', '')) #true
print(isSubsequence('a', '')) #false
print(isSubsequence('axc', 'ahbgdc')) #false