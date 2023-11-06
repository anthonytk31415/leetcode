## heaps 
## main heap property: 
## A[parent] >= A[i]



x = [None,1,2,3,4,5,6]

class MaxHeap: 
    def __init__(self) -> None:
        self.heap = [None]
        self.heap_size = 0
        self.front = 1
        # in this implementation, the heap starts at i = 1

    def print(self):
        print(self.heap[1:self.heap_size+1])

    def printAll(self):
        print(self.heap)

    @staticmethod
    def parent(i):
        return i//2

    @staticmethod
    def left(i):
        return 2*i

    @staticmethod
    def right(i):
        return 2*i + 1
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    # always insert at the end of the heap
    # will preserve the max heap property
    def insert(self, val):
        self.heap.append(val)
        self.heap_size +=1
        cur = self.heap_size  # i = current index
        parentOfCur = MaxHeap.parent(cur)
        while parentOfCur >0 and self.heap[cur] > self.heap[parentOfCur]:
            self.swap(cur, parentOfCur)
            cur = parentOfCur
            parentOfCur = MaxHeap.parent(cur)
        # will need to swap to maintain heap property

    
    def delete(self):
        if self.heap_size == 0:
            return 
        self.swap(1, self.heap_size)
        self.heap_size -=1
        cur = 1
        left = right = None
        if MaxHeap.left(cur) <= self.heap_size: left = MaxHeap.left(cur)
        if MaxHeap.right(cur) <= self.heap_size: right = MaxHeap.right(cur)
        # condition is: does cur have children? are the children valid? 
        while left or right:
            if left and self.heap[cur] < self.heap[left]:
                largest = left
            else: 
                largest = cur
            if right and self.heap[largest] < self.heap[right]:
                largest = right
            if largest != cur:
                self.swap(cur, largest)
                # define new current, left and right
                cur = largest
                left = right = None
                if MaxHeap.left(cur) <= self.heap_size: left = MaxHeap.left(cur)
                if MaxHeap.right(cur) <= self.heap_size: right = MaxHeap.right(cur)
            else:
                break
            



    # returns true or false whether the root is a max heap
    # def isMaxHeap(root):
    #     if root:
    #         res = []
    #         if root.left: 
    #             res.append(root.val >= root.left.val)
    #         if root.right:
    #             res.append(root.val >= root.right.val)
    #         return all(res + [Node.isMaxHeap(root.left), Node.isMaxHeap(root.right)])
    #     else: 
    #         return True

    # given an index i that might be a max heap, 
    # turn the tree from i onward into a max heap. 
    # this assumes that the children of i are max heaps
    def maxHeapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if left <= self.heap_size and self.heap[i] < self.heap[left]:
            largest = left
        else: 
            largest = i
        if right <= self.heap_size and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != i:
            self.swap(i, largest)
            self.maxHeapify(largest)

    ## requires array from 1-n; 0th index does nothing
    ## this takes an array and returns a heap object!
    def buildMaxHeap(arr,n):
        mHeap = MaxHeap()
        mHeap.heap = mHeap.heap + arr
        mHeap.heap_size = n
        for i in range(n//2,0,-1):
            mHeap.maxHeapify(i)
        return mHeap

    ## takes in an array, returns the array sorted
    def heapsort(arr, n):
        mHeap = MaxHeap.buildMaxHeap(arr, n)
        mHeap.print()
        for i in range(n, 1, -1):
            mHeap.swap(1,i)
            mHeap.heap_size -=1
            mHeap.maxHeapify(1)
        return mHeap

    


root = MaxHeap()
root.insert(10)
root.insert(20)
root.insert(5)
root.insert(16)
root.insert(22)
root.insert(17)
root.insert(19)
root.insert(35)
root.print()

root.delete()
# root.print()
root.delete()
# root.print()
root.delete()
root.delete()
root.delete()
root.delete()
root.delete()
root.delete()
root.printAll()

# arr = [1, 3, 19, 21, 15, 17, 8]
# # arr1 = MaxHeap.buildMaxHeap(arr, 7)
# arr1 = MaxHeap.heapsort(arr, 7)

# print(arr1.heap)


# root = Node(100)
# root.left = Node(50)
# root.right = Node(70)
# root.left.left = Node(30)
# root.left.right = Node(99)
# print(Node.isMaxHeap(root))

# def max_heapify

# def build_max_heap