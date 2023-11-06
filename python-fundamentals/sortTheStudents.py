def sortTheStudents(score, k):
    score.sort(key = lambda x: -x[k])
    return score

score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2

print(sortTheStudents(score, k))
