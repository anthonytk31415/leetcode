# def neighbors(i,j, m,n):
#     matrix = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
#     return list(filter(lambda x: x[0] <m and x[0]>=0 and x[1] <n and x[1] >=0, matrix))


# print(neighbors(1,2, 5,5))
# z1 = [[1,2],[3,3]]
# print(z1)
# print(z1[0][1])
# print(z1[1][0])
# z2 = list(filter(lambda x: x[0]==1, z1))
# print(z2)


# [1,2,3,4]
# [5,6,7,8]
# [9,10,11,12]

# (i-1)*(n) + j
# m = 3
# i, j = 3,1 --> 2*4 + 1 = 9
# 3,4 -> 2*4 + 4 = 12
# 1,4 -> 0*4 + 4 = 4

# 0,0


# class Helper:
#     blah = 1
#     def fun(self, string):
#         # self.
#         return 'hello ' + string

# print(Helper.fun('dummy', 'blah'))



# a = {'a':1}

# def myfn(z):
#     z['a'] = 2

# myfn(a)
# print(a['a'])

# a1 = myfn(a)
# print(a1)


a = {}

a[(0,0)] =1

print((0,0) in a)