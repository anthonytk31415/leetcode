# cycle: 
# - ensure you have enough water, then water the plant (update position, steps, capacity, next plant)
# - if you dont' have enough water, go to river, (update position, steps, capacity, next plant)

# O(n) time, O(1) space

def wateringPlants(plants, capacity):
    steps = 0
    cur_loc = -1
    cur_plant = 0
    cur_capacity = capacity
    while cur_plant < len(plants):
        # water the first plant
        if cur_capacity >= plants[cur_plant]:
            steps += abs(cur_plant - cur_loc)                   # walk from where you are to the plant
            cur_loc = cur_plant                                 # update location
            cur_capacity = cur_capacity - plants[cur_plant]     # update capacity
            cur_plant +=1    

        # not enough water so add steps to go walk back then go
        else:
            steps += abs(-1 - cur_loc)
            cur_loc = -1
            cur_capacity = capacity

    return steps

# plants = [2,2,3,3]
# capacity = 5

# plants = [1,1,1,4,2,3]
# capacity = 4

plants = [7,7,7,7,7,7,7]
capacity = 8

print(wateringPlants(plants, capacity))