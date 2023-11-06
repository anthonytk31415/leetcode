from collections import deque

conversions = {}
units = set()
# create for inches, feet, yards, miles

for unit1, unit2, factor in [('inches', 'feet', 1/12), ('feet', 'yards', 1/3), ('feet', 'miles', 1/5280)]:
    units.add(unit1)
    units.add(unit2)
    conversions[(unit1, unit2)] = factor

def bfs(unit1, unit2, num):
    visited = set()
    queue = deque()
    queue.append((unit1, num))
    visited.add(unit1)
    while queue: 
        for _ in range(len(queue)):
            unit, qty = queue.popleft()
            if unit == unit2: 
                return qty
            for unit1, unit2 in conversions: 
                factor = conversions[(unit1, unit2)]
                if unit1 == unit and unit2 not in visited:
                    visited.add(unit2)
                    queue.append((unit2, qty*factor))
                elif unit2 == unit and unit1 not in visited: 
                    visited.add(unit1)
                    queue.append((unit1, qty*(1/factor)))


print(bfs('inches', 'miles', 1.2))