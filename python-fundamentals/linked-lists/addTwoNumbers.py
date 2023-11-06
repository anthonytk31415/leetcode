class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        if self.val != None: 
            res = str(self.val) 
            next = self.next
            if isinstance(next, Node):
                return res + next.__str__()
            else: 
                return res

def addTwoNumbers(list1, list2):
    if not list2:
        return list1
    if not list1: 
        return list2

    head_res = Node()

    head1 = Node()
    head1.next = list1

    head2 = Node()
    head2.next = list2

    node1 = head1.next
    node2 = head2.next
    node_res = head_res     # this will always point to the most previous current digit

    carry = 0
    while node1 and node2: 
        curSum = node1.val + node2.val + carry        

        if curSum > 9:
            carry = 1
            curSum = curSum % 10        
        
        else:                       # <--- dont want to reset carry unless it's truly 0
            carry = 0
        
        node_res.next = Node(curSum)
        node1 = node1.next
        node2 = node2.next
        node_res = node_res.next
    
    while node1:
        curSum = node1.val + carry

        if curSum > 9:
            carry = 1
            curSum = curSum % 10    
        carry = 0

        node_res.next = Node(curSum)
        node1 = node1.next
        node_res = node_res.next

    while node2:
        curSum = node2.val + carry
        
        if curSum > 9:
            carry = 1
            curSum = curSum % 10    
        carry = 0

        node_res.next = Node(curSum)
        node2 = node2.next
        node_res = node_res.next

    return head_res.next
            



# lst1_dummy = Node()
# lst2_dummy = Node()

# node1 = lst1_dummy
# node2 = lst2_dummy

# for x in num1: 
#     node1.next = Node(x)
#     node1 = node1.next

# for y in num2: 
#     node2.next = Node(x)
#     node2 = node1.next

def printList(lst):
    node = lst
    while node: 
        print(node.val)
        node = node.next

def createLinkedListFromArr(arr):
    lst1_dummy = Node()
    node1 = lst1_dummy
    for x in arr[::-1]: 
        node1.next = Node(x)
        node1 = node1.next

    return lst1_dummy.next


num1 = [1,2,3,4,5,6]
num2 = [7,8,9]

lst1 = createLinkedListFromArr(num1)
lst2 = createLinkedListFromArr(num2)
# printList(lst1)
# printList(lst2)


added = addTwoNumbers(lst1, lst2)
# printList(added)

print(added)