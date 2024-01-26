def minimumCost(list):
    list.sort()
    return sum(list[:3])


nums = [1,2,3,12]
print(minimumCost(list))