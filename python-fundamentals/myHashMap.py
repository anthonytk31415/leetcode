# Implementation of Hash Map

# Our initial data store is an array with length of 19997 when is a large size. You'll 
# want an array large enough to cover all the range of values plus more to minimize and
# avoid collisions in lookup and keep lookup of your hash close to O(1), but at the cost
# of larger space. 

# We'll define a simple hash function: the index of our store will be:
# index = key * veryLargePrime %  length of hash table

# we'll store values at the index in the form of linked lists and keep the most recent 
# input at the head of the linked list. 

# - when we get, we'll hash to get to the index --> LL and traverse the LL to find key.
# - when we remove a value, we'll have to hash to find the index, traverse the LL to 
# find the key, then remove that node, (noting we also need to reattach prev to removed's 
# next). 
# - when we put, we get to the index >> LL. then remove the key value pair in the LL. 
# Then we create a new LL and put it in front of the LL and then rebind the LL to the 
# data[index] spot. 

# That's it!


class MyHashMap:

    class ListNode:
        def __init__(self, key, val, next=None):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self):
        self.length = 19997
        self.prime = 12582917
        self.data = [None for _ in range(self.length)]

    def hash(self, key):
        return self.prime * key % self.length


    def put(self, key: int, val: int) -> None:
        self.remove(key)
        newNode = self.ListNode(key, val)
        index = self.hash(key)
        newNode.next = self.data[index]
        self.data[index] = newNode

    def get(self, key: int) -> int:
        index = self.hash(key)
        node = self.data[index]
        while node: 
            if node.key == key: 
                return node.val
            node = node.next
        return -1 

    def remove(self, key: int) -> None:
        index = self.hash(key)
        node = self.data[index]
        prev = None

        while node: 
            if node.key == key: 
                if prev != None: 
                    prev.next = node.next
                    return 
                else: 
                    self.data[index] = node.next
                    return 
            else: 
                prev = node
                node = node.next






myHash = MyHashMap()
myHash.put(1,1)
myHash.put(2,2)
print(myHash.get(2))
print(myHash.get(3))
myHash.put(2,1)
print(myHash.get(2))
myHash.remove(2)
print(myHash.get(2))
