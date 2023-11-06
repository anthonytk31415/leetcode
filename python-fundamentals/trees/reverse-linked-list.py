# reverseList


def reverseList(node):
    prev = None
    new = node
    temp_next = node.next
    new.next = prev
    while temp_next:
        prev = node
        node = temp_next
        new = node
        temp_next = node.next
        new.next = prev
    return new

