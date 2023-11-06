# reorderList


# 0,1,2,3,4 -> 0,4,1,3,2
# 0,1,2,3 -> 0,3,1,2
# for n even: 
# for n odd: 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    if head.next == None:
        return head

    fast = slow = head

    # dummy = ListNode(0)
    # dummy.next = head

    lowerHalf = {}
    counter = 0
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        counter +=1
    # stopped at the median(odd) or lower of median (even)
    median = counter
    while slow.next:
        slow = slow.next
        counter +=1
        lowerHalf[counter] = slow
    ## start with beginning, then attach .next as lowerhalf[i], then iterate

    slow = head
    res = dummy = ListNode(0)
    for i in range(counter, median, -1):
        res.next = slow
        slow = slow.next
        res = res.next
        res.next = lowerHalf[i]
        res = res.next
        # print(i)

    if median %2 == 0: ## end with median if median is odd
        res.next = slow
        res = res.next
    res.next = None
    return dummy.next

root = ListNode(1)
root.next = ListNode(2)
# root.next.next = ListNode(3)
# root.next.next.next = ListNode(4)
# root.next.next.next.next = ListNode(5)

def traverse(root):
    node = root
    while node:
        print(node.val)
        node = node.next

# traverse(root)
# print(reorderList(root))
print(traverse(reorderList(root)))