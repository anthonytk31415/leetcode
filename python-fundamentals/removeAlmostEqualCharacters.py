def removeAlmostEqualCharacters(word):
    charValue = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    val = 0
    for char in alpha: 
        charValue[char] = val
        val += 1

    res = 0
    i = 0
    while i < len(word)-1:
        if abs(charValue[word[i]] - charValue[word[i+1]])  <= 1:
            res += 1
            i += 1
        i += 1
    return res


# word = "aaaaa"
# word = "abddez"
# word = "zyxyxyz"
# word = "ewveodc"
word = "ewveodcdovwevoveecdowowevowoddcocecdwvdwcdooeddedeeowvcovvvcvvdcevdoeoeoodcve"
      #   x   x   x     x x          x     x x   x x x x x   x   x   x x        x x  
     #   x   x
     #    x   x   
# dovwevoveecd"
# owowevowoddcocecdwvdwcdooeddedeeowvcovvvcvvdcevdoeoeoodcve"
print(removeAlmostEqualCharacters(word))