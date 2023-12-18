

from collections import deque
from heapq import heappush, heappop
from math import inf 
# class ExamRoom1:

#     def __init__(self, n):
#         self.n = n
#         self.seats = [] 
#         self.orderSeats = [-1] * n
#         self.order()

#     def order(self):
#         self.orderSeats = [-1] * self.n
#         # print(self.orderSeats)
#         if self.n == 1: 
#             return 
#         queue = deque()
#         self.orderSeats[0] = 0
#         self.orderSeats[self.n-1] = 1
#         mid = (0 + self.n - 1)//2
#         if self.orderSeats[mid] == -1: 
#             queue.append((0, self.n-1, mid))
#         i = 2
#         while queue: 
#             left, right, mid = queue.popleft()
#             self.orderSeats[mid] =  i
#             i += 1
#             for u, v in [(left, mid), (mid, right)]:
#                 curMid = (u + v) // 2
#                 if self.orderSeats[curMid] == -1:
#                     queue.append((u, v, curMid))


#         for i in range(len(self.orderSeats)):
#             heappush(self.seats, (self.orderSeats[i], i))


#     def seat(self):
#         seatVal, seatIdx = heappop(self.seats)
#         return seatIdx

#     def leave(self, p):
#         heappush(self.seats, (selforderSeats[p], p))
#         return 






# this O(1) operation, nlogn is too slow


# class ExamRoom:
#     def __init__(self, n):
#         self.n = n
#         self.seats = [0] * n
#         self.numSeats = 0
#         self.nextSeat = []
#         self.defineOrder()

#     def defineOrder(self):
#         def binarySplit(i, j, mid, dist):
#             tempNextSeat.append((-dist, mid))
#             for u, v in [(i, mid), (mid, j)]:
#                 if v - u > 1: 
#                     binarySplit(u, v, (u + v) //2, (u + v)//2 - u)
#             return 
        
#         tempNextSeat = []
#         if self.numSeats == 0:            
#             tempNextSeat.append((-self.n, 0))
#             tempNextSeat.append((-(self.n - 1) , self.n-1))
#             if self.n > 1: 
#                 binarySplit(0, self.n-1, (self.n-1 + 0) // 2, (self.n-1 + 0 )// 2)
#         else: 
#             left = -1
#             for right in range(len(self.seats)):
#                 if self.seats[right] == 1:
#                     if left == -1: 
#                         if right > 0: 
#                             tempNextSeat.append((-right, 0))
#                             if right > 1: 
#                                 binarySplit(0, right, right//2, right//2)
#                     else: 
#                         if right - left > 1: 
#                             binarySplit(left, right, (left + right)// 2, (left + right)// 2 - left)
#                     left = right

#             if left < len(self.seats) - 1:
#                 tempNextSeat.append(( -(len(self.seats)-1 - left), len(self.seats) - 1))
#                 if len(self.seats) - 1 - left > 1:
#                     binarySplit(left, len(self.seats)-1, (left + len(self.seats)-1)//2, (left + len(self.seats)-1)//2 - left) 

#         tempNextSeat.sort(key = lambda x: (x[0], x[1]))
#         self.nextSeat = deque(tempNextSeat)

#     def seat(self):
#         if self.numSeats >= self.n:
#             return 
#         _, idx = self.nextSeat.popleft()
#         self.seats[idx] = 1
#         self.numSeats += 1
#         return idx

#     def leave(self, p):
#         self.seats[p] = 0
#         self.numSeats -= 1       
#         self.defineOrder()
#         return 


from bisect import insort

class ExamRoom:
    def __init__(self, n):
        self.n = n
        self.seats = []             # we will append all 1's here


    def seat(self):
        seats, n = self.seats, self.n
        if not seats: 
            res = 0
        else: 
            maxDist = seats[0]                  # default to putting a person at seat 0 with distance of the index seats[0]
            res = 0                             # if there's a 1 at index 0, then dist is 0; if theres a 1 at index k, dist = k
            for a, b in zip(seats, seats[1:]):
                if (b - a)//2 > maxDist: 
                    maxDist = (b - a) // 2   
                    res = (b + a) // 2          # take midpoint
            if n - 1 - seats[-1] > maxDist:     # condition where 1,0,.., 0 at the end; insert "1" at n - 1
                maxDist = n - 1 - seats[-1]
                res = n - 1

        insort(seats, res)
        return res

    def leave(self, p):
        self.seats.remove(p)
        return 




blah = ExamRoom(10)
# print(blah.orderSeats)
print(blah.seats)
blah.seat()
blah.seat()
blah.seat()
blah.leave(0)
blah.leave(4)
blah.seat()
blah.seat()
blah.seat()
blah.seat()
blah.seat()
blah.seat()
blah.seat()
blah.seat()
blah.seat()
blah.leave(0)
blah.leave(4)
blah.seat()
blah.seat()
blah.leave(7)
blah.seat()
blah.leave(3)
blah.seat()
blah.leave(3)
blah.seat()
blah.leave(9)
# print(blah.nextSeat)
# print(blah.seats)
# blah.seat()
# # blah.leave(0)
# # blah.leave(8)
# # blah.seat()
# # blah.seat()
# # blah.leave(0)
# # blah.leave(8)
# # blah.seat()
# # blah.seat()
# # blah.leave(2)
# blah.seat()
# blah.seat()
# print(blah.seats)
# blah.leave(6)
# print(blah.seats)
# blah.seat()
# blah.seat()
# blah.seat()
# blah.seat()
# blah.seat()

print(blah.seats)
