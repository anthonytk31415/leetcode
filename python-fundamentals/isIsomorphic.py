## faster, but not fast enough, stil O(n) where n = len(s) + len(t)
# def isIsomorphic(s, t):
#     def convert_iso(s):
#         s_new = ''
#         s_dict = {}
#         s_tracker = s
#         alpha = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ '
#         s_counter = iter(alpha)
#         for x in s_tracker: # replace string in s with a digit; remove 
#             if x not in s_dict:
#                 sc_next = next(s_counter)
#                 s_dict[x] = sc_next
#         for x in s: 
#             s_new = s_new + (s_dict[x])
#         return s_new
#     s_new = convert_iso(s)
#     t_new = convert_iso(t)
#     print(s_new, t_new)
#     return s_new == t_new



def isIsomorphic(s, t):
    s_new = ''
    s_dict = {}
    s_tracker = s
    alpha = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ '
    s_counter = iter(alpha)
    for x in s_tracker: # replace string in s with a digit; remove 
        if x not in s_dict:
            sc_next = next(s_counter)
            s_dict[x] = sc_next
    for x in s: 
        s_new = s_new + (s_dict[x])

    t_new = ''
    t_dict = {}
    t_tracker = t
    # alpha = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ '
    t_counter = iter(alpha)
    for x in t_tracker: # replace string in s with a digit; remove 
        if x not in t_dict:
            tc_next = next(t_counter)
            t_dict[x] = tc_next
    for x in t: 
        t_new = t_new + (t_dict[x])

    print(s_new, t_new)
    return s_new == t_new



# alpha = 'abcdefghijklmnopqrstuvwxyz'
# s_cycle = iter(alpha)
# t_cycle = iter(alpha)

# print(next(s_cycle))
# print(next(t_cycle))
# print(next(t_cycle))
# print(next(t_cycle))
# print(next(s_cycle))


# a = 'anthony'
# a = a.replace('n','z')
# print(a)



print(isIsomorphic('paper', 'title'))
print(isIsomorphic('aaab', 'cccd'))
print(isIsomorphic('a', 'z'))
print(isIsomorphic('abra', 'kadabra'))
print(isIsomorphic('anthony', 'heavens'))
print(isIsomorphic("qwertyuiop[]asdfghjkl;'\\zxcvbnm,./", "',.pyfgcrl/=aoeuidhtns-\\;qjkxbmwvz"))