

# Rehashing allows for an even distribution of the hash table; 

# class ListNode:
#     def __init__(self, val):
#         self.val = val 
#         self.next = None

class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.cur_size = 0


    def getHashCode(self, key):
        return hash(key)
    
    def getIndex(self, key):
        return self.getHashCode(key) % self.size

    def get(self, key):
        hash_val = self.getIndex(key)
        bucket = self.table[hash_val]
        for i, (k, v) in enumerate(bucket):
            if k == key: 
                return v                        # you find the key
        raise KeyError(key)                     # you can't find the key
        

    def put(self, key, value):                  # update the entrry if te key exists
        hash_val = self.getIndex(key)
        bucket = self.table[hash_val]
        for i, (k, v) in enumerate(bucket):
            if i == key: 
                bucket[i] = (key, value)
                return
        bucket.append((key, value))             # add the new key value pair to the bucket                                 
        self.cur_size +=1

    def needRehashing():
        pass 

    def remove(self, key):
        hash_val = self.getIndex(key)
        bucket = self.table[hash_val]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i] 
                self.cur_size -=1
                return 
        raise KeyError(key)

    def length(self):                                 # length of the hash table
        return self.cur_size

    def isEmpty(self):
        return self.cur_size == 0


lookup = HashMap(3000)
lookup.put('ant', 'man')
lookup.put('wanda', 'vision')

print(lookup.get('ant'))
print(lookup.get('wanda'))


print(lookup.remove('wanda'))
lookup.put('super', 'cereal')
print(lookup.get('super'))
print(lookup.length())