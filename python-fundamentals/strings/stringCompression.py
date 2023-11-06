

def compress(chars):
    curLetter = chars[0]
    curCount = 1
    j = -1                              # represents the end of the updated chars
    for i in range(1, len(chars)): 
        c = chars[i]
        if c != curLetter:
            j +=1
            chars[j] = curLetter
            if curCount > 1:
                for string_count_letter in str(curCount):
                    j +=1
                    chars[j] = string_count_letter
            curCount = 1
            curLetter = c
        else: 
            curCount +=1

    j +=1
    chars[j] = curLetter
    if curCount > 1:
        for string_count_letter in str(curCount):
            j +=1
            chars[j] = string_count_letter

    # print(chars[:j+1])
    return len(chars[:j+1])
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","b","b","c","c","c"]
compress(chars)