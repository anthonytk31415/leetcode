# minheap 
# i = 1       # i rempresents the next thing to be popped if the min heap is empty

# i will always be greater than elements in the minheap

# when you pop, if the set/minheap is empty, then pop i, increment i+=1
# if it is not empty, then pop the to top element from the minheap and remove it from the set

# when you add element x, add it to the min heap and to a set but only if x is not in minheap/set and x < i 

# popping will be a worst case O(log n)
# adding will be O(log n)
# memory will 

from heapq import heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = []
        self.minHeapSet = set()
        self.i = 1

    def popSmallest(self) -> int:
        if not self.minHeap:
            res = self.i
            self.i +=1
        else: 
            res = heappop(self.minHeap)
            self.minHeapSet.remove(res)
        return res

    def addBack(self, num: int) -> None:
        if num < self.i and num not in self.minHeapSet:
            heappush(self.minHeap, num)
            self.minHeapSet.add(num)
    
