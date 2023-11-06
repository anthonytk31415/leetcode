from heapq import heappush, heappop

class SeatManager:

    def __init__(self, n: int):
        arr = [x for x in range(1, n+1, 1)] 
        self.seats = []
        for x in arr: 
            heappush(self.seats, x) 

    def reserve(self) -> int:
        return heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats, seatNumber)



arr = [x for x in range(10)]

heappop(arr)
print(arr)
heappush(arr, 0)
print(arr)

print(heappop(arr))
print(heappop(arr))
print(heappop(arr))
print(heappop(arr))
print(arr)