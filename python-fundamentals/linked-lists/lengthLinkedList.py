
def pairSum(head):
    def lengthLinkedList(head):
        n = 0
        cur = head
        while cur: 
            n += 1
            cur = cur.next
        return n

    n = lengthLinkedList(head)