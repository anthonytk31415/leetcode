class MinHeap:
    # implementing a 1-indexed array; so vaies from 1 -n
    def __init__(self, arr): 
        self.heap = arr
        self.heapSize = len(arr)-1
        self.buildMinHeap(self.heapSize)

    def left(self, i):
        return 2* i

    def right(self, i):
        return 2*i + 1

    def parent(self, i):
        return i // 2

    def __str__(self):
        return f'{self.heap}'
    
    # given i, its children are minheaps
    def minHeapify(self, i):                # this is the percolate downward
        l = self.left(i)
        r = self.right(i)
        a = self.heap
        # find smallest
        if l <= self.heapSize and a[l] < a[i]:
            smallest = l
        else:
            smallest = i
        if r <= self.heapSize and a[r] < a[smallest]:
            smallest = r
        if i != smallest:
            a[i], a[smallest] = a[smallest], a[i]
            self.minHeapify(smallest)
        
    def buildMinHeap(self, n):
        self.heapSize = n
        for i in range(n//2, 0, -1):
            self.minHeapify(i)

    def heappop(self):
        if self.heapSize >0 : 
            a[1], a[self.heapSize] = a[self.heapSize], a[1]
            res = self.heap.pop()
            self.heapSize -=1
            self.minHeapify(1)        
            return res 
        else: 
            return -1

    def heappush(self, val):
        self.heap.append(val)
        self.heapSize +=1
        i = self.heapSize
        while i > 1 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def peek(self):
        return self.heap[1]


a = [None, 4, 1, 3]

minHeap = MinHeap(a)

print(minHeap, 'size: ', minHeap.heapSize)

print(minHeap.peek())
print(minHeap.heappop())
print(minHeap)
minHeap.heappush(10)
print(minHeap)
minHeap.heappush(-1)
print(minHeap)
minHeap.heappush(12)
print(minHeap)
minHeap.heappush(5)
print(minHeap)