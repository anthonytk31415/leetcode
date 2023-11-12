

from collections import defaultdict

def findHighAccessEmployees(access_times):
    
    graph = defaultdict(list)
    for employee, access_time in access_times: 
        graph[employee].append(int(access_time))
    
    res = []
    for employee in graph.keys(): 
        graph[employee].sort()
        times = graph[employee]
        print(len(times), len(times)- 2)
        for i in range(len(times) - 2):

            if times[i] <= times[i + 1] < times[i] + 100 and times[i] <= times[i + 2] < times[i] + 100: 
                res.append(employee)
                break

    return res


# access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
# access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]

access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]
print(findHighAccessEmployees(access_times))