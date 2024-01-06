class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    prevVal = None
    dummy = ListNode()
    dummy.next = head

    node = head
    prevNode = dummy
    count = 1
    lastInt = dummy 

    while node: 
        if node.val != prevNode.val: 
            if count == 1: 
                lastInt.next = prevNode
                lastInt = prevNode
            count = 1
        else: 
            count += 1            

        prevNode = node
        node = node.next

    print(count, prevNode.val)

    if count == 1: 
        # print("this")
        lastInt.next = prevNode
    # elif count > 1 and lastInt == dummy: 
    #     dummy.next = None

    return dummy.next

# arr = [1,1]
# arr = [1]
arr = []
# arr = [1,2,3,3,4,4,4,4,5]

def buildLinkedList(arr):
    dummy = ListNode()
    node = dummy
    for num in arr: 
        node.next = ListNode(num)
        node = node.next
    return dummy.next

def printLinkedList(head):
    node = head
    while node: 
        print(node.val)
        node = node.next

x = buildLinkedList(arr)
# printLinkedList(x)

y = deleteDuplicates(x)
printLinkedList(y)
# print(y.val if y else y)