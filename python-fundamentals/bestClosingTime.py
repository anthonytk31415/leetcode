def bestClosingTime(customers):

    penalty = 0
    for cust in customers: 
        if cust == "N": penalty += 1
    
    minPenalty = penalty
    minTime = len(customers)
    for i in range(len(customers)-1, -1, -1):
        cust = customers[i]
        if cust == "Y": penalty += 1
        elif cust == "N": penalty -=1
        if penalty < minPenalty:
            minPenalty = penalty
        if penalty <= minPenalty: minTime = i
    return minTime

customers = "YYNY"

print(bestClosingTime(customers))