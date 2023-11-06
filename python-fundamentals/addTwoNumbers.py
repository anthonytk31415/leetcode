# addTwoNumbers

# - add the digits, make a new node, if there's a remainder or if l1 or l2 are
# - put the remainder directly in the next node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## my first solution; O(n) running time 
## O(n) space complexity

## 
def addTwoNumbers(l1, l2):
    ## if the number is not null, add them together. if > 9: find remainder and carry it to the next iteration

    prevRes = None
    head =  ListNode() 
    curRes = head
    remainder = None
    cur1, cur2 = l1, l2

    while cur1 or cur2 or remainder: 
        if prevRes: prevRes.next = curRes
        curVal = 0
        # add remainder
        if remainder: curVal += remainder
        remainder = None
        # sum valid values    
        for x in [cur1, cur2]:
            if x:
                curVal += x.val

        # deal with remainder to carry to next node
        if curVal > 9: 
            remainder = 1
            curVal = curVal - 10

        # assign node the value, prepare 'prev' for next iteration
        curRes.val = curVal
        prevRes = curRes

        # prepare the cur res for the next iteration; assign new cur1 and cur2 values
        curRes = ListNode()
        if cur1: cur1 = cur1.next
        if cur2: cur2 = cur2.next
    return head


# this solution is so smooth; 
# it uses a pointer to the head of the list node that you'll return 
# and it does so to kick off the while loop
# there's use of //= as well as modulo directly in ListNode to apply the carry progressively 

def addTwoNumbers2(l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry > 0:
        if l1: 
            carry += l1.val
            l1 = l1.next
        if l2: 
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //=10
    return dummy.next