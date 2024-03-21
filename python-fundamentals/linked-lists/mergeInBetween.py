def mergeInBetween(list1, a, b, list2):
    
    dummy = ListNode()
    dummy.next = list1
    node = dummy
    
    for _ in range(a):
        node = node.next
    before_a = node

    for _ in range((b - a + 1)):
        node = node.next
    after_b = node.next

    # find end of list2
    node = list2
    while node and node.next:
        node = node.next
    endList2 = node

    before_a.next = list2
    endList2.next = after_b

    return dummy.next

