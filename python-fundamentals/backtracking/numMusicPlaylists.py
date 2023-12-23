from collections import Counter, defaultdict
from heapq import heappush, heappop
from math import factorial


def numMusicPlaylists(n, goal, k): 
    songsPlayed = Counter()
    playlist = [None]*goal
    songLastPlayed = defaultdict(list)
    memo = {}

    def dfs(numSongs):
        if numSongs == goal: 
            # count[0] += 1
            print(0, playlist)
            return 1

        elif (goal - numSongs) <= n - len(songsPlayed):
            n_star = goal - numSongs
            k_star = n - len(songsPlayed)
            if (n_star, k_star) not in memo:
                memo[(n_star, k_star)] = factorial(n_star)/factorial(n_star - k_star)
            # count[0] += memo[(n_star, k_star)]
            print(1, playlist, "memo: ", memo[(n_star, k_star)])
            return memo[(n_star, k_star)]

        candidates = []
        for u in range(n):
            if (u not in songsPlayed) or (u in songsPlayed and (goal - numSongs) > n - len(songsPlayed) and numSongs > songLastPlayed[u][-1] + k): candidates.append(u)

        if len(songsPlayed) == n and len(candidates) == n - k: 
            # count[0] += k**(goal - numSongs)
            print("2", playlist, (n-k)**(goal - numSongs))
            return k**(goal - numSongs)

        res = 0
        for u in candidates: 
            playlist[numSongs] = u
            songsPlayed[u] += 1
            songLastPlayed[u].append(numSongs)

            res += dfs(numSongs + 1)
            
            playlist[numSongs] = None
            songsPlayed[u] -=1
            if songsPlayed[u] == 0: del songsPlayed[u]
            songLastPlayed[u].pop()

            if numSongs == 0: 
                res *= len(candidates)
                break 

            # if u not in songsPlayed: 
            #     res *= len(candidates)
            #     break 
        return res
    return dfs(0)
    # return count[0]

# print(numMusicPlaylists(3, 3, 1))
# print(numMusicPlaylists(2, 3, 0))       # 6
print(numMusicPlaylists(3, 5, 1))       # 150
# print(numMusicPlaylists(3, 10, 1)) # 1530


# def dummy(x):

#     myHash = defaultdict(list)
#     def helper(d):
#         myHash[x].append(1)
#         return 
#     helper(x)
#     print(myHash)
#     return 
# print(dummy(22))