from collections import defaultdict 

# sliding window problem 
# the sliding window in this case never shrinks! once it has found its max width, it'll 
# continue to have its max width, but that just makes things 
# a bit confusing

def totalFruit(fruits):
    basketCount = defaultdict(int)      # fruit 
    bLim = 2
    fruitCount, maxFruits = 0, 0
    left = 0
    for i, fruit in enumerate(fruits):
        if fruit not in basketCount:
            while len(basketCount) == bLim: 
                # increment left and remove items until you have enough room: 
                basketCount[fruits[left]] -=1
                fruitCount -= 1
                if basketCount[fruits[left]] == 0: 
                    del basketCount[fruits[left]]
                left += 1

        basketCount[fruit] += 1
        fruitCount += 1
        maxFruits = max(maxFruits, fruitCount)
    return maxFruits

fruits = [1,0,1,4,1,4,1,2,3]

print(totalFruit(fruits))