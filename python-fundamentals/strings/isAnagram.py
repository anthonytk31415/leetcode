# isAnagram



# s = str, t = str

from collections import Counter
def isAnagram(s, t):

    s_count = Counter(s)
    t_count = Counter(t)
    return s_count == t_count