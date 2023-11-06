
def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))

    res = []
    for a, b in people: 
        res.insert(b, [a,b])

    return res



# people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]

people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]

print(reconstructQueue(people))
# ans = [4,0], [5,0], [2,2], [3,2], [1,4], [6,0]

