from math import inf 

# gotta worry about edge cases. 
# This is a classic dp problem


def videoStitching(clips, time):
    times = [-inf for _ in range(time + 1)]
    dp = [inf] * (time + 1)
    for start, end in clips:
        if start > time: continue
        if end > times[start]: 
            times[start] = end

    for i in range(len(times) - 1, -1, -1):
        if i == len(times) - 1: dp[i] = 0
        elif times[i] == -inf or i == times[i]: dp[i] = inf
        else: 
            dp[i] = 1 + min(dp[i+1: times[i] + 1])
    return -1 if dp[0] == inf else dp[0] 

# clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
# time = 9

# clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
# time = 10

# clips = [[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]]
# time = 5

clips = [[17,18],[25,26],[16,21],[3,3],[19,23],[1,5],[0,2],[9,20],[5,17],[8,10]]
time = 15

# clips = [[0,1],[1,2]]
# time = 5

# print(clips[1:3])

print(videoStitching(clips, time))
