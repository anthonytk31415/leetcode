
# a = defaultdict()
# a[1] = {'a': 0, 'b':2} 
# a[2] = {'a': 3, 'b': 0}
# a[3] = {'a': -1,'b':2}
# b = sorted(a, key=lambda x:( a[x]['b'], a[x]['a']))
# print(b[0])

from collections import defaultdict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = defaultdict()
        self.min = None
        self.time = 0

    def get(self, key: int) -> int:
        #needs to return value if key exists, -1 if not
        if key not in self.storage:
            return -1
        else: 
        # also needs to keep track of frequency
            self.storage[key]['time'] = self.time
            self.time +=1
        # assign new min value 
            x = sorted(self.storage, key = lambda x: self.storage[x]['time'])
            self.min = sorted(self.storage, key = lambda x: self.storage[x]['time'])[0]
            return self.storage[key]['value']

    def put(self, key: int, value: int) -> None:
        # check for deletion requirement
        if key not in self.storage and len(self.storage) == self.capacity:
            del self.storage[self.min]
        
        self.storage[key] = {'value': value, 'time': self.time}
        # update the min
        self.min = sorted(self.storage, key = lambda x: self.storage[x]['time'])[0]
        self.time +=1

## example
# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)
# lRUCache.put(2, 2)
# lRUCache.get(1)
# lRUCache.put(1, 5)
# print(lRUCache.get(1))
# # lRUCache.put(4, 4)
# # print(lRUCache.get(1))
# # print(lRUCache.get(3))
# # print(lRUCache.get(4))

# print(lRUCache.storage, lRUCache.min)

