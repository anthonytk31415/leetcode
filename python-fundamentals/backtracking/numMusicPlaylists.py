from collections import Counter, defaultdict
from heapq import heappush, heappop
from math import factorial


def numMusicPlaylists(n, goal, k): 

    count = [0]
    songsPlayed = Counter()
    playlist = [None]*goal
    songLastPlayed = defaultdict(list)
    memo = {}
    def dfs(numSongs):

        if numSongs == goal: 
            count[0] += 1
            return 
        elif (goal - numSongs) <= n - len(songsPlayed):
            n_star = goal - numSongs
            k_star = n - len(songsPlayed)
            if (n_star, k_star) not in memo:
                memo[(n_star, k_star)] = factorial(n_star)/factorial(n_star - k_star)
            count[0] += memo[(n_star, k_star)]
            return 

        for u in range(n):
            if ((u not in songsPlayed) or 
                (u in songsPlayed and (goal - numSongs) > n - len(songsPlayed) and numSongs > songLastPlayed[u][-1] + k)): 
                playlist[numSongs] = u
                songsPlayed[u] += 1
                songLastPlayed[u].append(numSongs)
                dfs(numSongs + 1)
                playlist[numSongs] = None
                songsPlayed[u] -=1
                if songsPlayed[u] == 0: del songsPlayed[u]
                songLastPlayed[u].pop()
    dfs(0)
    return count[0]

# print(numMusicPlaylists(3, 3, 1))
# print(numMusicPlaylists(2, 3, 0))

print(numMusicPlaylists(3, 25, 1))


# def dummy(x):

#     myHash = defaultdict(list)
#     def helper(d):
#         myHash[x].append(1)
#         return 
#     helper(x)
#     print(myHash)
#     return 
# print(dummy(22))