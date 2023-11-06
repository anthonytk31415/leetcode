# for product of integers (neg or pos),
# we'll keep a running total of the largest product and will evaluate the product each iteration as add more integers
# we'll keep two trackers: a running min and running max
# key: if we hit a negative, min becomes max, and max becomes min (at least for integers)
# at each iteration, we'll assess the true max = max(old true max, current max) which will 
# take care of hitting a zero or a negative number 


from math import inf
def maxProduct(nums):
	mini, maxi, res = 1, 1, -inf
	for n in nums:
		a = mini * n
		b = maxi * n
		mini = min(a, b, n)
		maxi = max(a, b, n)
		res = max(res, maxi)
	return res


# x = [-1, 0, 0, -2, 0]
# x = [2,-5,-2,-4,3, 0]
x = [2,-5,-2,0,3,2,8,2,-4,3, 0]
# x = [1,2,-2,-3,2,-5,1,4,8] 

# x = [2,3,-2,4]
# x = [-2,0,-1]
print(maxProduct(x))

            


# def maxProduct(nums):
#     curMax = curMin = res = nums[0]
#     for i in range(1,len(nums)): 
#         a = max(curMax*nums[i], curMin*nums[i], nums[i])
#         b = min(curMax*nums[i], curMin*nums[i], nums[i])
#         curMax = a
#         curMin = b
#         res = max(res, curMax)
#     return res
            


        



# def prod(arr):
#     if arr == []:
#         return 0
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         res = 1
#         for x in arr:
#             res *= x
#         return res

# print(prod([1,2]))
# print(prod([]))
# print(prod([1]))
# print(prod(x))


# def maxProduct(nums):
#     # base case 
#     if len(nums) == 1:
#         return nums[0]
#     reduced = []
#     curPos = None
#     curNeg = None
#     chain = []
#     def prod(arr):
#         if arr == []:
#             return 0
#         if len(arr) == 1:
#             return arr[0]
#         else:
#             res = 1
#             for x in arr:
#                 res *= x
#             return res
#     for x in nums:
#         # print(x)
#         if x > 0: 
#             if curNeg==None:
#                 if curPos!= None:   
#                     curPos = curPos * x
#                 else: curPos = x
#             else: 
#                 if curPos: 
#                     chain.append(curPos)
#                 chain.append(curNeg)
#                 curPos = x
#                 curNeg = None
#         elif x < 0: 
#             if curNeg == None:
#                 curNeg = x
#             else:
#                 if curPos != None: 
#                     curPos = curPos * x * curNeg
#                 else: 
#                     curPos = x * curNeg
#                 curNeg = None
#         elif x == 0: 
#             if curPos != None:
#                 chain.append(curPos)
#             if curNeg != None:
#                 chain.append(curNeg)
#             reduced.append(chain)
#             reduced.append([])
#             chain = []
#             curPos = None
#             curNeg = None
#     #do things at the end
#     if curPos != None:
#         chain.append(curPos)
#     if curNeg != None:
#         chain.append(curNeg)
#     reduced.append(chain)
#     print(reduced)
#     res = []
#     for x in reduced: 
#         if len(x) == 0:
#             res.append(0)
#         elif prod(x) > 0: 
#             res.append(prod(x))
#         else: 
#             res.append(max(x))
#     # print(reduced)
#     return max(res) 

