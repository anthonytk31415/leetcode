from collections import defaultdict

def longestArithSeqLength(nums):

    graph = defaultdict(defaultdict)

    # keep track of all delta(i,j) for the earliest occurrence of delta within i
    # graph i gives you a dictionary with keys = delta, value = index of the earliest delta

    # i = index
    # graph[i] = dict of all deltas
    # graph[i][delta] = index where going from i to j gives you delta
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            delta = nums[j] - nums[i]
            if delta not in graph[i]:
                graph[i][delta] = j

    # visitedDelta = defaultdict(list)
    overallMax = 0
    deltaMax = None

    # for each i: dfs the delta and keep track of node i's successors 
    # each time you visit a node, at one to the end
    memo = {}
    
    def dfs(u, delta):
        if (u, delta) in memo: return memo[(u, delta)]

        res = 1
        if delta in graph[u]:
            v = graph[u][delta]
            res += dfs(v, delta)

        memo[(u, delta)] = res
        return res

    overallMax = 0
    overallDelta = []

    for i in range(len(nums)):
        deltas = graph[i]
        for delta in deltas: 
            curMax = dfs(i, delta)
            if curMax > overallMax:
                overallMax = curMax
                overallDelta = [delta]
                
            elif curMax == overallMax:
                overallDelta.append(delta)

    return overallMax

# nums = [3,6,9,12]
# nums = [9,4,7,2,10]
# nums = [20,1,15,3,10,5,8]




nums = [44,46,22,68,45,66,43,9,37,30,
 50,67,32,47,44,11,15,4,11,6,
 20,64,54,54,61,63,23,43,3,12,
 51,61,16,57,14,12,55,17,18,25,
 19,28,45,56,29,39,52,8,1,21,
 17,21,23,70,51,61,21,52,25,28]

# nums = [15,4,11,6,

#  55,17,18,25,
#  19,28,45,56,29,39,52,8,1,21,
#  17,21,23,70,51,61,21,52,25,28]


print(longestArithSeqLength(nums))
# def longest_arith_seq_subsequence(arr):
#     n = len(arr)
#     if n <= 1:
#         return arr  # Return the entire array if it's too short to form a subsequence.

#     # Initialize a dictionary to store the length and subsequence of the longest arithmetic subsequence ending at each index.
#     dp = [{} for _ in range(n)]
#     max_length = 2  # Initialize the maximum length to 2 (minimum possible length for an arithmetic subsequence).

#     for i in range(n):
#         for j in range(i):
#             diff = arr[i] - arr[j]
#             if diff in dp[j]:
#                 # Extend the subsequence.
#                 dp[i][diff] = (dp[j][diff][0] + 1, dp[j][diff][1] + [arr[i]])
#             else:
#                 # Start a new subsequence.
#                 dp[i][diff] = (2, [arr[j], arr[i]])
#             if dp[i][diff][0] > max_length:
#                 max_length = dp[i][diff][0]
#                 longest_subsequence = dp[i][diff][1]

#     return longest_subsequence

# arr = [
#     44, 46, 22, 68, 45, 66, 43, 9, 37, 30,
#     50, 67, 32, 47, 44, 11, 15, 4, 11, 6,
#     20, 64, 54, 54, 61, 63, 23, 43, 3, 12,
#     51, 61, 16, 57, 14, 12, 55, 17, 18, 25,
#     19, 28, 45, 56, 29, 39, 52, 8, 1, 21,
#     17, 21, 23, 70, 51, 61, 21, 52, 25, 28
# ]

# result = longest_arith_seq_subsequence(arr)
# print("Longest arithmetic subsequence:", result)