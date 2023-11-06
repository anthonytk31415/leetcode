# longestCommonSubsequence

def longestCommonSubsequence(text1, text2):
    # you want t1 > t2
    if text1 > text2:
        t1 = text1
        t2 = text2
    else: 
        t1 = text2
        t2 = text1

    t1_index = {} ### {'a':[0], 'n':[1,5], 't':[2],'h':[3],'o':[4],'y':[6]}
    for char, index in enumerate(t1):
        if char not in t1_index:
            t1_index[char] = [index]
        else: 
            t1_index[char].append(index)
    
    t2_chain = set()
    ## for each letter of t2: 
    ## elements in t2_chain: {'index': 0, 'length': 1}
    for x in t2:
        if x in t1_index: 
            curIndex = t1_index[x]
            # check for each index in t2_chain if curIndex > index  
            for y in t2_chain: 



### incomplete, use that grid method