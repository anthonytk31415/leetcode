def findWinners(matches):
    allPlayers = set()
    lost = set()
    lostMultiple = set()
    # lost - lostMultiple = lost once 
    # all - lost = winners
    for u, v in matches: 
        allPlayers.add(u)
        allPlayers.add(v)
        if v in lost: lostMultiple.add(v)
        lost.add(v)
    return [list(lost - lostMultiple), list(allPlayers - lost)]


# a = set([1,2,3])
# b = set([2,3,4])
# print(list(a - b))

# print([list(a), list(b)])



matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

print(findWinners(matches))