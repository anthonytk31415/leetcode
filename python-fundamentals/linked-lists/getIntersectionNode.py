class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode2(headA, headB): 
    nodeA = headA
    nodeB = headB 

    lookupA = {}
    lookupB = {}

    while nodeA:
        lookupA[nodeA] = True
        nodeA = nodeA.next
    while nodeB: 
        lookupB[nodeB] = True
        nodeB = nodeB.next
    
    nodeA = headA
    while nodeA: 
        if nodeA in lookupB: 
            return nodeA
        nodeA = nodeA.next
    return False

### --------------------------------------------------------
def getIntersectionNode3(headA, headB): 
    lenA = 0
    lenB = 0
    nodeA = headA
    nodeB = headB
    while nodeA != None: 
        lenA +=1
        nodeA = nodeA.next
    while nodeB != None: 
        lenB +=1
        nodeB = nodeB.next
    nodeA = headA
    nodeB = headB
    if lenA > lenB: 
        for _ in range(lenA - lenB):
            nodeA = nodeA.next
    else: 
        for _ in range(lenB - lenA):
            nodeB = nodeB.next
    while nodeA: 
        print(nodeA.val, nodeB.val)
        if nodeA == nodeB: 
            return nodeA
        else: 
            nodeA = nodeA.next
            nodeB = nodeB.next



def getIntersectionNode(headA, headB): 
    curA,curB = headA,headB
    lenA,lenB = 0,0
    while curA is not None:
        lenA += 1
        curA = curA.next
    while curB is not None:
        lenB += 1
        curB = curB.next
    curA,curB = headA,headB
    if lenA > lenB:
        for i in range(lenA-lenB):
            curA = curA.next
    elif lenB > lenA:
        for i in range(lenB-lenA):
            curB = curB.next
    while curB != curA:
        curB = curB.next
        curA = curA.next
    return curA






def buildListNode(arr):
    head = ListNode(0)
    node = head
    while arr: 
        node.next = ListNode(arr[0])
        node = node.next
        arr = arr[1:]
    return head.next


c = [8,4,5]

# a = [4,1,8,4,5]
a = [4,1]
# b = [5,6,1,8,4,5]
b = [5,6,1]
rootA = buildListNode(a)
rootB = buildListNode(b)
rootC = buildListNode(c)

rootA.next.next = rootC
rootB.next.next.next = rootC
print(rootA.next.next.next.val)
print(rootA.next.next.next == rootB.next.next.next.next)

print(getIntersectionNode(rootA, rootB).val)