from collections import deque

def addTwoNumbers(l1, l2):

    def linkedToDeque(head):
        d = deque()
        node = head
        while node: 
            d.appendleft(node.val)
            node = node.next
        return d

    def arrToLinkedList(arr):
        head = ListNode(arr[0])
        node = head
        for i, num in enumerate(arr[1:]):
            node.next = ListNode(num)
            node = node.next
        return head

    d1 = linkedToDeque(l1)
    d2 = linkedToDeque(l2)
    # print(d1, d2)

    res = deque()
    n = 0
    curCarry, nextCarry = 0, 0
    while d1 and d2: 
        fullSum = d1.popleft() + d2.popleft() + curCarry
        if fullSum > 9: nextCarry += 1
        res.appendleft(fullSum % 10)
        curCarry, nextCarry = nextCarry, 0

    while d1: 
        fullSum = d1.popleft() + curCarry
        if fullSum > 9: nextCarry += 1
        res.appendleft(fullSum % 10)
        curCarry, nextCarry = nextCarry, 0

    while d2: 
        fullSum = d2.popleft() + curCarry
        if fullSum > 9: nextCarry += 1
        res.appendleft(fullSum % 10)
        curCarry, nextCarry = nextCarry, 0
    if curCarry: 
        res.appendleft(curCarry)


    res = list(res)
    return arrToLinkedList(res)



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        cur = self 
        res = []
        while cur: 
            res.append(str(cur.val))
            cur = cur.next
        return ", ".join(res)


def arrToLinkedList(arr):
    head = ListNode(arr[0])
    node = head
    for i, num in enumerate(arr[1:]):
        node.next = ListNode(num)
        node = node.next
    return head

arr1 = [7,2,4,3]
arr2 = [3,5,6,4]
l1, l2 = arrToLinkedList(arr1), arrToLinkedList(arr2)


print(addTwoNumbers(l1, l2))