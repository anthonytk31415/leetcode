class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(employees, id):
    # build adjacency list 
    eList = {}
    for employee in employees: 
        eList[employee.id] = employee

    def dfs(id):
        res = eList[id].importance
        for child in eList[id].subordinates:
            res += dfs(child)
        return res

    return dfs(id)