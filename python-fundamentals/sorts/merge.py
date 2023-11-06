# merge 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode() # at the end, we will return a.next as that is the pointer to the head
        cur = a
        i = list1
        j = list2
        while bool(i) and bool(j):
            if i.val < j.val:
                cur.next = i
                i = i.next
            else:
                cur.next = j
                j = j.next
            cur = cur.next
        while bool(i):
            cur.next = i
            i = i.next
            cur = cur.next
        while bool(j):
            cur.next = j
            j = j.next
            cur = cur.next
        return a.next

# list1 = [1,2,4] 
# list2 = [1,3,4]


# print(Solution.mergeTwoLists('a', list1, list2))

