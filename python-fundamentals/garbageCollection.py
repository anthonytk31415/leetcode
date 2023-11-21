from collections import Counter

def garbageCollection1(garbage, travel):
    loadLast = {}                           # wil include the last index that load was seen at so you know when to stop
    for i, gLoad in enumerate(garbage):
        garbage[i] = Counter(gLoad)
        for load in ["M", "P", "G"]:
            if load in garbage[i]:
                loadLast[load] = i

    totalMinutes = 0
    for load in ["M", "P", "G"]:
        if load in loadLast: 
            for i in range(len(garbage)):
                if load in garbage[i]:
                    totalMinutes += garbage[i][load]
                # add travel
                if i == loadLast[load]:
                    break 
                else: 
                    totalMinutes += travel[i]

    return totalMinutes


def garbageCollection(garbage, travel):



garbage = ["G","P","GP","GG"]
travel = [2,4,3]
garbage = ["MMM","PGM","GP"]
travel = [3,10]

print(garbageCollection(garbage, travel))