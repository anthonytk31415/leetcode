class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitListToParts(head, k):
    from math import floor 

    def lengthLinkedList(head):
        n = 0
        cur = head
        while cur: 
            n += 1
            cur = cur.next
        return n

    n = lengthLinkedList(head)

    ## determine length of list: n
    minLength = floor(n/k)
    remainder = n % k 

    ## remainder = n % k // do an if statement during the partition 
    cur = head
    prev = ListNode()
    prev.next = cur
    res = []

    for _ in range(k):
        curSegment = cur
        numIterations = minLength
        if remainder > 0: 
            numIterations += 1
            remainder -= 1
        
        for _ in range(numIterations): 
            prev = cur
            if cur: 
                cur = cur.next
            else: 
                cur = None

        ## snip the end off and append
        if prev: prev.next = None

        res.append(curSegment)

    return res



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


res = splitListToParts(head, 4)
for x in res: 
    print("start new node")
    cur = x
    while cur: 
        print(cur.val)
        cur = cur.next


# O(n) solution for time; O(1) for space

    