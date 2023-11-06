def minimumRefill(plants, capacityA, capacityB):


    left = 0
    right = len(plants) - 1

    curLeft, curRight = capacityA, capacityB

    refills = 0
    while left <= right: 
        alice = True
        bob = True
        if left == right: 
            if curLeft >= curRight: 
                bob = False
            else: 
                alice = False
        
        if alice: 
            # water is sufficient:
            if curLeft < plants[left]:
                curLeft = capacityA
                refills += 1
            curLeft -= plants[left]
            left += 1
                        
        if bob: 
            if curRight < plants[right]:
                curRight = capacityB
                refills += 1
            curRight -= plants[right]
            right -= 1
    
    return refills

# plants = [2,2,3,3]
# capacityA = 5
# capacityB = 5


plants = [2,2,3,3]
capacityA = 3
capacityB = 4

print( minimumRefill(plants, capacityA, capacityB))