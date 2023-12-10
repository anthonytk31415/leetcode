def countTestedDevices(batteryPercentages):
    count = 0
    for i, b in enumerate(batteryPercentages):
        if b > 0: 
            count += 1
            for j in range(i+1, len(batteryPercentages)):
                batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
    return count

batteryPercentages = [1,1,2,1,3]

batteryPercentages = [0,1,2]
print(countTestedDevices(batteryPercentages))