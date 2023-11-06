# rotateRight

def rotateRight(head, k):
    # deal with base cases: 
    if not head or k == 0: 
        return head
    ## find length of head
    cur = head 
    n = 0 
    while cur: 
        n +=1
        cur = cur.next
    ## find k modulo head
    k = k % n
    # deal with base cases: 
    if k == 0 or n == 1: 
        return head
    ## find the suffix and presuffix; presuffix.next = None; then traverse to end of suffix, attach end of suffix.next to head
    suffix = head
    for _ in range(n-k-1):
        suffix = suffix.next
    preSuffix = suffix
    suffix = suffix.next
    preSuffix.next = None

    cur = suffix
    while cur.next: 
        cur = cur.next
    cur.next = head

    return suffix