## constructing a full max heap


# usingheaps: turn the array into heap using heapify
# perform deletion k times
# the last k items are sorted in descending order via deletion; grab the a[-k] element

# heapify takes O(n) time for n elements
# O(1) space
# deletion takes O*(k*log(n)) times 
# total time O(k*log(n))

## given an array 
def findKthLargest(nums, k):
    heap = Heap(nums)
    buildmaxheap(heap, len(nums))
    for _ in range(k):
        deletion(heap)
    return heap.heap[-k]


class Heap:
    def __init__(self, arr=[]):
        self.heap = [None] + arr
        self.heapsize = len(arr)

def parent(i): 
    return i//2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def swap(node, i, j):
    node.heap[i], node.heap[j] = node.heap[j], node.heap[i]

## given a node where its children are heaps, heapify the tree
def maxheapify(node, i):
    left_i = left(i)
    right_i = right(i)
    if left_i <= node.heapsize and node.heap[i] < node.heap[left_i]:
        largest = left_i
    else: 
        largest = i
    if right_i <= node.heapsize and node.heap[largest] < node.heap[right_i]:
        largest = right_i
    if largest != i: 
        swap(node, i, largest)
        maxheapify(node, largest)


def buildmaxheap(node, n):
    for x in range(n//2, 0, -1):
        maxheapify(node, x)


def deletion(node):
    # swap 1 with last element in the heap
    # reduce node size
    # max heapify with 1 
    if node.heapsize == 0:
        return
    last = node.heapsize
    node.heapsize -=1
    swap(node, 1, last)
    maxheapify(node, 1)

## sample calls

arr=[1,4,2,6,8,10,3,7]

node = Heap(arr)
buildmaxheap(node, len(arr))
deletion(node)
deletion(node)
deletion(node)
deletion(node)
deletion(node)
print(node.heap)



print(findKthLargest(arr, 3))



###### lets use the python functions 