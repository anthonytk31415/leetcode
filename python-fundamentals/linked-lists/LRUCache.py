# tricks: 
# doubly linked lists; recent adds and updates go to the head; 


class DoubleLinkedList:
    def __init__(self, val=None, key=None):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

from collections import defaultdict

class LRUCache:
    def __init__(self, capacity: int):
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.cap = capacity
        self.lookup = defaultdict()

        self.head.next = self.tail
        self.tail.prev = self.head

    # lookup will be used for: key = key, value = node
    # checking whether your lookup has capacity via length == capacity: for put  

    ## get: 
    ## is it in the lookup? then return the node val; do del/ins to "update"
    def get(self, key: int) -> int:
        if key not in self.lookup: 
            return -1
        else: 
            node = self.lookup[key]
            self.deletion(node)
            self.insertion(node)
            return node.val

    ## put
    ## if val not in lookup: (i.e. need to insert)
    ## need to free capacity
    ## if length == capacity, (1) remove LRU from the tail (reattached tail.prev.prev) and the (2) lookup
    ## then insert new at head; update the pointers, insert in lookup, pointing to the lookup 
    ## 
    ## if val in lookup: 
    ## (1) update the dict and the node itself with the new val
    ## (2) delete the node from list, reattach pointers, move node to the head
    
    # insert node at the head
    def insertion(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def deletion(self, node):
    ## reassign neighbor pointers of deleted node
        node.prev.next, node.next.prev = node.next, node.prev 

    ## if you update the node, the node is used so it requires a del/ins
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.deletion(node)
            self.insertion(node)            
        if key not in self.lookup:
            node = DoubleLinkedList(value, key)
            if len(self.lookup) == self.cap:
                del self.lookup[self.tail.prev.key]
                self.deletion(self.tail.prev)
            self.lookup[key] = node
            self.insertion(node)
    
x = LRUCache(2)
print(x.put(1,1))
print(x.put(2,2))
print(x.get(1))
print(x.put(3,3))
print(x.get(2))
print(x.put(4,4))
print(x.get(1))
print(x.get(3))
print(x.get(4))


# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
# 2 capacity, none, none, 2/1 removed, 1/1 removed, 1 = -1 2 => -1