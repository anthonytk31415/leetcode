# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        if not slow.next: return True
        slowC = 0
        reverse = {}
        reverse[slowC] = slow.val
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            slowC +=1
            reverse[slowC] = slow.val
        if not fast.next:
            # means you're on the median and total nodes = fastC; # skip over median
            reverseC = slowC - 1
        else: 
            reverseC = slowC
        slow=slow.next
        slowC +=1
        while slow:
            if slow.val != reverse[reverseC]:
                return False
            slowC +=1
            reverseC -=1
            slow = slow.next
        return True


root = ListNode(1)
root.next = ListNode(1)
root.next.next = ListNode(1)
root.next.next.next = ListNode(1)

print(Solution.isPalindrome('yo', root))