class MyHashSet:

    class ListNode:
        def __init__(self, key, next=None):
            self.key = key
            self.next = next

    def __init__(self):
        self.length = 3000000
        self.factor = 12345678910987654321
        self.arr = [None]*self.length

    def hashcode(self, key):
        return key * self.factor % self.length

    # add the node in the front of the LL
    def add(self, key: int) -> None:
        if self.contains(key): return 

        idx = self.hashcode(key)
        node = self.arr[idx]
        newListNode = self.ListNode(key, node)
        self.arr[idx] = newListNode


    def remove(self, key: int) -> None:
        if (self.contains(key) == False): return 

        idx = self.hashcode(key)
        node = self.arr[idx]
        
        prev = None
        newNode = None
        while node: 
            if node.key == key: 
                if prev == None: 
                    self.arr[idx] = node.next
                    return 
                else: 
                    prev.next = node.next
                    return 

    # check the LL if any node = key
    def contains(self, key: int) -> bool:
        idx = self.hashcode(key)
        node = self.arr[idx]
        while node:
            if node.key == key:
                return True
            node = node.next 
        return False
