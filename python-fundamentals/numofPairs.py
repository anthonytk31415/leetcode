# 105

## is x equal to first part of target? 
## --> if so, is second part of target (x - 1) in nums? (build a hash table?)


## note you can allow duplicates so accommodate for this

# you coan do this in O(n) with a hash table 

def numOfPairs(nums, target):
    lookup = {}
    # create hash table with the occurrence as the value => 'string': # occurrence 
    for x in nums: 
        if x not in lookup: 
            lookup[x] = 1
        else: 
            lookup[x] +=1
    
    counter = 0
    # for each x in nums: check if x is equal to that part of target
    for x in nums: 
        if x == target[:len(x)]:
            x_comp = target[len(x):]
            if x == x_comp: 
                if lookup[x] > 1:       # case when first half equals second half
                    counter += (lookup[x_comp] - 1)
            elif x_comp in lookup:                  # "normal" pair matching
                counter += (lookup[x_comp])
    return counter
# nums = ["777","7","77","77"]
# target = "7777"


nums = ["1","1","1"]
target = "11"
print(numOfPairs(nums, target))