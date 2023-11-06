# maximum subarray


# def maxSubArray(nums):
#     # print('starting...')

#     chain = nums[0]
#     curMax = nums[0]
    
#     for i in range(1,len(nums)):
#         a = nums[i]
#         b = 0
#         #ensure you have a pair to check
#         if i+1 < len(nums):
#             b = nums[i+1]
#         # print(f'chain = {chain}, curMax = {curMax}, a={a}, b={b}')
#         if a >=0 and (chain == None or chain < 0 ):
#             chain = a
#         elif a >= 0:
#             if chain == None:
#                 chain = a
#             else:
#                 chain += a
#         elif a < 0 and a+b >= 0:
#             if chain == None:
#                 chain = a
#             else:
#                 chain += a
#         if (chain != None) and (chain > curMax):
#             curMax = chain 
#         if a + b < 0:
#             chain = None
#         # print(f'chain end = {chain}')
#     return curMax

# nums = [-2, -1]


# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [5,4,-1,7,8]
# nums = [5,4,-1, -1,7,8, 9, 3]
# print(maxSubArray(nums))

# print(sum(nums))



# def reduce(nums):
#     container = []
#     current = 0

#     if len(nums) <= 1:
#         return nums

#     for x in nums:
#         if x >= 0 and current >= 0:
#             current += x
#         elif x >= 0 and current < 0:
#             container.append(current)
#             current = x
#         elif x < 0 and current >= 0:
#             container.append(current)
#             current = x
#         elif x < 0 and current < 0:
#             current +=x
#     if current != 0:
#         container.append(current)
#     return container

# x = [1,2,-2,-2,1,-1,2,-2,5,6]

# # x = [1,2,-2,-2,1,-1,2,-2,0]
# print(reduce(x))



# AT solutiion
# def maxSubArray(nums):
#     if len(nums) == 0:
#         return nums
#     chain = None
#     curMax = None
#     for n in nums:
#         # print(f'n = {n}, old chain = {chain}, old curMax = {curMax}')
#         if chain == None:
#             chain = n
#         else: 
#             chain = chain + n
#         if curMax == None:
#             curMax = n
#         if chain < 0:
#             chain = None
#         # assign max        
#         if not(chain):
#             curMax = max(curMax, n)
#         else: 
#             curMax = max(chain, curMax, n)
#         # print(f'n = {n}, new chain = {chain}, new curMax = {curMax}')
#     return curMax




def maxSubArray(nums):
    print(nums)
    if len(nums) <= 1:
        return sum(nums)
    
    if len(nums) == 2:
        [a,b] = nums
        print(a,b)
        if a >=0 and b >= 0:
            print([a+b])
            return maxSubArray([a + b])
        else:
            print([max(nums)])
            return maxSubArray([max(nums)])

    else: 
        a = 0 
        b = len(nums) - 1
        q = (a + b)//2
        left = nums[a:q+1]
        right = nums[q+1: b+1]
        print (f'{left}, {right}')
        print([maxSubArray(left) + maxSubArray(right)])
        return maxSubArray([maxSubArray(nums[a:q+1]), maxSubArray(nums[q+1: b+1])])



# nums = [-2, -1, 4, 5]
# nums = [-2, -1]
# nums=[-1]
# nums=[0]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [5,4,-1,7,8]
nums = [5,4,-1, -1,7,8, 9, 3]
# nums = [5,4,-1, -1,7,-1, -10, 2, 2, 3]


print(maxSubArray(nums))