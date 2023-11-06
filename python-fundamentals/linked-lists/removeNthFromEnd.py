# removeNthFromEnd
# beware of the base cases

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#this is lightning fast but uses hash tables and not the linked lists structure 
def removeNthFromEnd(head, n):
    lookup = {}
    node = head
    i = 0
    while node:
        lookup[i] = node
        node = node.next
        i +=1
    end = i
    n_star = end - n
    if (n_star -1) in lookup:
        # print(f'lookup: {lookup}, n*: {n_star}, end: {end}')
        if (n_star + 1) in lookup:
            lookup[n_star - 1].next = lookup[n_star + 1]
        else: 
            lookup[n_star -1].next = None
    else: 
        head = head.next
    return head

## code another solution





# def removeNthFromEnd(head, n):
    # fast = slow = start = head
    # fast_c = slow_c = 0
    # while fast.next and fast.next.next: 
    #     fast = fast.next.next
    #     slow = slow.next
    #     fast_c +=2
    #     slow_c +=1
    # if fast.next != None: 
    #     end = fast_c + 2
    #     alpha = slow_c + 2
    # else: 
    #     end = fast_c + 1
    #     alpha = slow_c +1
    # # print(alpha, n)
    # if alpha == n and n== 1:
    #     return 
    # if alpha > n: ## N from end node is after midpoint; from slow, get there
    #     for _ in range(alpha - n - 1-1):
    #         slow = slow.next
    # else: 
    #     # print(end, n)
    #     slow = head ## reuse slow slow to start over and traverse to the N from end node, which is less than midway
    #     for _ in range(end - n-1-1):
    #         slow = slow.next
    # print(slow.val)
    # if not slow.next:
    #     slow.next = None
    # elif slow.next and slow.next.next == None:
    #     # print('executing 2')
    #     slow.next = None
    # else: 
    #     slow.next = slow.next.next
    # return start

root = ListNode(1)
# root.next = ListNode(2)
# root.next.next = ListNode(3)
# root.next.next.next = ListNode(4)
# root.next.next.next.next = ListNode(5)


def traverse(root):
    node = root
    while node:
        print(node.val)
        node = node.next

# traverse(root)
z = removeNthFromEnd(root, 1)
print('traversing:')
traverse(z)