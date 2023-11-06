class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# helper will return the head and the tail 

def flatten(head):
    def helper(link):
        head = Node()
        node = link 
        head.next = node 
        while node: 

            if node.child: 
                node_after_child = node.next
                child_head = helper(node.child)
                child_head.prev = node
                node.next = child_head
                while node and node.next: 
                    node = node.next
                node.next = node_after_child
                node_after_child.prev = node
            node = node.next

        node = head
        while node: 
            node.child = None
            node = node.next
        return head.next
    return helper(head)