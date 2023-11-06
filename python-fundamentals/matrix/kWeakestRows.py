# # k weakest rows in matrix

# # Time: O(nlogn for the sort)
# # Space: O(1); reuse and transform the mat


# # def kWeakestRows(mat, k): 
# #     mat = [sum(x) for x in mat]
# #     # print(f'sum: {mat}')
# #     mat = list(enumerate(mat))              #enumerate gievs you (index, x)
# #     mat.sort(key = lambda x: x[1])  
# #     print(mat)

# #     return [x[0] for x in mat[:k]]

a = [3,1,4]


# mat = [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]] 

# k = 3

# print(kWeakestRows(mat, k))