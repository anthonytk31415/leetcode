class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    #base case
    if left == right: 
        return head

    dummy = ListNode()
    dummy.next = head
    cur = head
    for _ in range(1, left-1):
        cur = cur.next          #get to L-1

    new_head = cur
    new_tail = cur.next         # tail of the reversed

    # set up the loop[
    cur = cur.next              # start at beg of reversed list
   
    while left < right: 


    new_head.next = cur
    new_tail.next = prev

    return dummy.next 



def reverseBetween(head, left, right):

    l, r = left - 1, right-1
    arr = []
    node = head
    while node: 
        arr.append(node)
        node = node.next
    arr = arr[:l] + list(reversed(arr[l:r+1])) + arr[r+1:]
    for i in range(1, len(arr)):
        arr[i-1].next = arr[i]
    arr[-1].next = None
    print([x.val for x in arr])
    return arr[0]
    

root = ListNode(3)
root.next = ListNode(5)
print(reverseBetween(root, 1,2))

