## largest perimeter


# a1 < a2 + a3 for any side of the triangle
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        z = sorted(nums, reverse=True)
        for i in range(len(z) - 3):
            print(i)
            if z[i] < z[i+1] + z[i+2]:
                return z[i] + z[i+1] + z[i+2]
        return 0


# def largestPerimeter(a):
#     import math
#     def merge(a, p, q, r):
#         # print('calling merge')
#         # print(a)
#         # print('{0}, {1}, {2}'.format(p,q,r))
#         len_left = q - p + 1
#         len_right = r - q 
#         # make the left and right copies of a
#         # print('coordinates - [{0},{1}]; [{2}, {3}]'.format(p,q,q+1,r))
#         # print('left {0}, right {1}'.format(len_left, len_right))
#         left = a[p: q+1] # don't forget the indeces don't include the end, so you add one
#         right = a[q+1: r+1] 
#         # print(left)
#         # print(right)
#         i = 0
#         j = 0
#         k = p
#         while i < len_left and j < len_right:
#             if left[i] <= right[j]:
#                 a[k] = left[i]
#                 i = i + 1
#             else:
#                 a[k] =  right[j]
#                 j = j + 1
#             k = k + 1
#         while i < len_left:
#             a[k] = left[i]
#             i = i + 1
#             k = k + 1
#         while j < len_right:
#             a[k] = right[j]
#             j = j + 1
#             k = k + 1
#         # print(a)
#     def mergesort(a, p, r):
#         if p >= r:
#             return 
#         q = math.floor( (p + r)/2 )
#         # print(q)
#         mergesort(a, p, q)
#         mergesort(a, q+1, r)
#         merge(a, p, q, r)
#     mergesort(a, 0, len(a)-1)
#     print(a)



# take first two; 9, 6,
# 9 - 6 = 3
# check entries > 3 starting with largest one

# 9, 8, 2 --> 19
# 6, 6, 6 --> 18
# 8, 6, 6 -- > 20
# 9, 8, 6, 6, 2

# find the first candidate starting the largest one
# if none exist, go to the next one
# 

