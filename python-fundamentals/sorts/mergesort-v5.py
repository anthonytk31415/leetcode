# mergesort practice


def merge(a,b):
    lenA , lenB = len(a), len(b)
    res = [0]*(lenA + lenB)
    i = j = k = 0
    while i < lenA and j < lenB:
        if a[i] < b[j]: 
            res[k] = a[i]
            i +=1
        else: 
            res[k] = b[j]
            j +=1
        k +=1
    while i < lenA:
        res[k] = a[i]
        i +=1
        k +=1
    while j < lenB:
        res[k] = b[j]
        j +=1
        k +=1
    return res

def mergesort(a):
    if len(a) == 0: 
        return None
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])    
    merged = merge(left, right)
    return merged


a = [6,3,2,7,9,11,4,1,0,5]

b = mergesort(a)
# print(b)

def insertionsort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -=1
        a[j+1] = key


insertionsort(a)
print(a)


## heapsort

## 

class Heap:
    def __init__(self, arr=[]):
        self.heap = [None] + arr
        self.heapsize = len(arr)
    def print(self):
        print(self.heap)

def parent(i):
    return i//2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def swap(heap, i, j):
    heap.heap[i], heap.heap[j] = heap.heap[j], heap.heap[i]

# node = Heap([30, 20, 10, 5, 3, 8, 7])
# node = Heap([30, 2, 10, 5, 3, 8, 7])
# print(node.heapsize)
# node.print()


#given node i, and children of i heaps, make heap i a max heap
def maxheapify(heap, i):
    left_i = left(i)
    right_i = right(i)
    if left_i <= heap.heapsize and heap.heap[i] < heap.heap[left_i]:
        largest = left_i
    else: 
        largest = i
    if right_i <= heap.heapsize and heap.heap[largest] < heap.heap[right_i]:
        largest = right_i
    if largest != i:
        swap(heap, i, largest)
        maxheapify(heap, largest)


arr = [1,19, 9, 11, 30]
# print(node.heapsize)
# node.print()

# maxheapify(node, 2)
# node.print()

# given an array, return a max heap
# O(log n) 

def buildmaxheap(arr):
    node = Heap(arr)
    n = node.heapsize
    for i in range(n//2, 0, -1):
        maxheapify(node, i)
    return node


node = buildmaxheap(arr)


def heapsort(arr):
    node = buildmaxheap(arr)
    n = node.heapsize
    for i in range(n, 1, -1):
        swap(node, 1, i)
        node.heapsize -=1
        maxheapify(node, 1)
    return node




# given a heap, insert a new element by inserting at the end and then swapping to top 
def insertion(heap, val):
    heap.heap.append(val)
    heap.heapsize +=1
    cur = heap.heapsize
    cur_parent = parent(cur)
    while heap.heap[cur_parent] < heap.heap[cur]:
        swap(heap, cur_parent, cur)
        cur = cur_parent
        cur_parent = parent(cur)


insertion(node, 12)
# node.print()


# given a heap, delete the max, return the max
def deletion(head):
    i = head.heapsize
    swap(head, 1, i)
    max = head.heap[i]
    head.heapsize -= 1
    maxheapify(head, 1)
    return max 

# max nodes = 2**(h+1) - 1

## uses deletion
def heapsort2(arr):
    node = buildmaxheap(arr)
    for _ in range(node.heapsize, 1, -1):
        n = node.heapsize
        deletion(node)
    return node

# node = heapsort2(arr)
# node.print()

node.print()
x = deletion(node)
node.print()
print(x)


