# canCompleteCircuit

# this works but is too slow
# sum of gas > sum of cost if a solution exists; 
# if there is, then 
def canCompleteCircuit(gas, cost):
    if sum(gas) - sum(cost) <0: 
        return -1
    index = 0
    reserve = 0
    for i in range(len(gas)):
        reserve += (gas[i] - cost[i])
        if reserve < 0:
            index = i + 1
            reserve = 0    
    return index 
    


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

# gas = [2,3,4]
# cost = [3,4,3]

print(canCompleteCircuit(gas, cost))