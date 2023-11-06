# codesignal2 practice
# square
# 2023-05-11

print('q2: ')

# from collections import deque

# def solution(queryType, query):

#     storage = {}
#     res = 0

#     for cur_qt, cur_q in zip(queryType, query):

#         if cur_qt == 'insert':
#             x, y = cur_q
#             storage[x] = [y]
        
#         elif cur_qt == 'get':
#             x = cur_q[0]
#             if x in storage: 
#                 res += storage[x][0]

#         elif cur_qt == 'addToKey':
#             x_plus = cur_q[0]
#             collisions = deque()
#             collisions_skipping_set = set()
#             for x in list(storage.keys()): 
#                 if x + x_plus in storage:
#                     if x + x_plus not in collisions_skipping_set:
#                         collisions.append([x + x_plus, storage[x + x_plus]])
#                         collisions_skipping_set.add(x + x_plus)
#                         storage[x + x_plus] = storage[x]
#                         del storage[x]

#                 elif x not in collisions_skipping_set:
#                     storage[x + x_plus] = storage[x]
#                     del storage[x]

#             # print('storage b4 coll: ', storage, collisions_skipping_set)
#             while collisions: 
#                 x, val = collisions.popleft()
#                 # print('this', x, val)
#                 storage[x + x_plus] = val



#         elif cur_qt == 'addToValue':
#             y = cur_q[0]
#             for x in storage:
#                 storage[x][0] += y
    

#         # print(cur_qt, cur_q, storage, res)
#     return res 


from collections import deque

def solution(queryType, query):

    storage = {}
    res = 0
    key_delta = 0
    value_delta = 0
    for cur_qt, cur_q in zip(queryType, query):

        if cur_qt == 'insert':
            x, y = cur_q
            storage[x - key_delta] = y - value_delta
        
        elif cur_qt == 'get':
            x = cur_q[0]
             
            res += storage[x - key_delta] + value_delta 

        elif cur_qt == 'addToKey':
            to_add = cur_q[0]
            key_delta += to_add

        elif cur_qt == 'addToValue':
            to_add = cur_q[0]
            value_delta += to_add
    

        # print(cur_qt, cur_q, storage, res)
    return res 







# queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
# query = [[1, 2], [2, 3], [2], [1], [3]]

# queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"]
# query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]]
# print(solution(queryType, query))

# queryType = ["insert", 
#  "insert", 
#  "addToValue", 
#  "addToKey", 
#  "get"]
# query  = [[1,2], 
#  [2,3], 
#  [2], 
#  [1], 
#  [3]]

queryType = ["insert", 
 "get", 
 "insert", 
 "addToValue", 
 "addToValue", 
 "addToValue", 
 "insert", 
 "addToKey", 
 "get", 
 "insert"]
query = [[2,1], 
 [2], 
 [1,3], 
 [-1], 
 [0], 
 [3], 
 [4,-5], 
 [3],
  [4], 
 [1,1]]
print(solution(queryType, query))

# queryType = ["insert", "addToValue", 'get', 'insert', 'addToKey', 'get', 'get', 'insert', 'addToValue',  "get"]
# query = [[1,2], [3], [1], [9, 12], [2], [11], [3], [0,2], [4], [0]]
# print(solution(queryType, query))