from collections import Counter, defaultdict

# just be careful with your hash tables and sort this shit

def rankTeams(votes):
    ranking = [defaultdict(int) for _ in range(len(votes[0]))]              
    teams = set(list(votes[0]))

    for vote in votes: 
        for place, team in enumerate(vote):
            ranking[place][team] += 1

    allTeamScores = []
    for team in teams: 
        teamScore = []
        for place in ranking: 
            placeScore = -place.get(team, 0)
            teamScore.append(placeScore)
        teamScore.append(team)
        allTeamScores.append(teamScore)
    allTeamScores.sort()
    idx = len(teams)
    res = "".join([x[idx] for x in allTeamScores])
    return res

votes = ["ABC","ACB","ABC","ACB","ACB"]
team = set(list(votes[0]))
# print(team)
print(rankTeams(votes))