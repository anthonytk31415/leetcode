def findJudge(n, trust):
    trustees = set([x[0] for x in trust])
    print(trustees)
    if len(trustees) == n:
        return -1
    people = set([x for x in range(1,n+1)])  
    potential_judge = people - trustees
    print(potential_judge)
    cond2 = set([x[0] for x in trust if x[1] in potential_judge])
    print(trustees == cond2)
    if len(potential_judge) == 1 and trustees == cond2:
        for x in potential_judge:
            return x
    return -1

print(findJudge(3, [[1,3],[2,3]]))
print(findJudge(3, [[1,3],[2,3],[3,1]]))