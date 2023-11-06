def restoreIpAddresses(s):
    res = set()

    def helper(s, path_arr, res):
        print(path_arr)
        if s and len(path_arr) == 4: 
            return 
        elif not s and len(path_arr) == 4:
            res.add('.'.join(path_arr))
            return 
        elif not s and len(path_arr) < 4: 
            return 
        else: 
            for x in [1,2,3]:
                partial = s[:x]
                after_partial = s[x:]
                if (x == 2 or x == 3) and partial[0] == '0':
                    continue
                if 0 <= int(partial) <= 255:
                    helper(after_partial, path_arr + [partial], res)

    helper(s, [], res)
    return res
# s = "0000"

s = "101023"
print(restoreIpAddresses(s))