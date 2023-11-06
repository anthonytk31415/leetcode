# keep an array of a,e,i,o,u next paths
# instantiate n = 0 as [1,1,1,1,1]
# and this keeps track of how many vowel[i] paths will be created at the next i
# after each i, add to each vowel destination more paths based on the current path

# so "a" new paths = "e" prev + "i" prev + "u" prev and so on
# so this becomes an O(n) time 


def countVowelPermutation(n): 

    path = [1,1,1,1,1]
    updatedPath = [1,1,1,1,1]
    curSum = 0
    i = 0 
    while i < n: 
        curSum = sum(path)
        updatedPath[0] = path[1] + path[2] + path[4]
        updatedPath[1] = path[0] + path[2]
        updatedPath[2] = path[1] + path[3]
        updatedPath[3] = path[2]
        updatedPath[4] = path[2] + path[3]
        path = [x for x in updatedPath]
        i += 1

    return curSum % (10**9 + 7)


print(countVowelPermutation(200))