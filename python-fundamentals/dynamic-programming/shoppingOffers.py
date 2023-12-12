# so this monstrosity of a backtracking problem works. 

def shoppingOffers(price, special, needs):
    minPrice = [sum([x*y for x, y in zip(price, needs)])]

    def dfs(curVal):
        # Check Terminal Value
        if all([x == 0 for x in needs]): 
            if curVal < minPrice[0]: minPrice[0] = curVal
            return 

        # Add another item, recurse. 
        for i in range(len(special)):
            sp = special[i]
            spItems, spVal = sp[:-1], sp[-1]

            # Chek valid move. 
            priceCheck = curVal + spVal <= minPrice[0]
            itemCheck = all([x - y >= 0 for x, y in zip(needs, spItems)])
            if priceCheck and itemCheck: 
                # make move
                for j in range(len(needs)):
                    needs[j] -= spItems[j]
                # recurse
                dfs(curVal + spVal) 
                # unmake move
                for j in range(len(needs)):
                    needs[j] += spItems[j]

        # finish with a la carte after possibly adding a special
        curVal += sum([x*y for x, y in zip(needs, price)])
        if curVal < minPrice[0]: minPrice[0] = curVal
        return 

    dfs(0)
    return minPrice[0]

# price = [2,3,4]
# special = [[1,1,0,4],[2,2,1,9]]
# needs = [1,2,1]

# price = [2,5]
# special = [[3,0,5],[1,2,10]]
# needs = [3,2]


price = [4,3,2,9,8,8]
special = [[1,5,5,1,4,0,18],[3,3,6,6,4,2,32]]
needs = [6,5,5,6,4,1]


print(shoppingOffers(price, special, needs))


# the general trick for backtracking
def backtrack(inputs): 
    if isASolution():
        processSolution()
    else: 
        candidates = constructCandidates()
        for c in candidates:
            makeMove()
            backtrack(inputs + c)
            unmakeMove()
        
            if (finished): 
                return 


