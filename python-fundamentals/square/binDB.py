from heapq import heappush, heappop
from collections import defaultdict, deque


class Trie:
    def __init__(self, val):
        self.val = val
        self.children = [None for _ in range(10)]       # ith entry is for digit = i
        self.isEntry = False
        self.data = {'prop1': [], 'prop2': []}

class BinDB:
    def __init__(self):
        # self.data = defaultdict(lambda: {'prop1': [], 
        # 'prop2': []})   ## key = bin, value = [], a priority queue that returns the most important upload data

        self.data = Trie(None)      # instantiate the root of the Trie with no data and None as the value
        self.props = ['prop1', 'prop2']

    # there should be a priority; and a mapping of source type and priority 
    # lets assume that we can create a separate mapping of priority

    # also, let's assume 
    # Q: how do w e know that when we grab data from multiple sources that they are from the same BIN


    # we assume that the priority is given; we can create a function that does sorce > priority later

    # bin: 123456
    # priority: 1
    # uploadData= {'prop1': 'data1', 
    #              'prop2': 'data2'}


    # for this assmption, based on the partial updates and sources portion, we don't know how we'll receive data from sources
    # so lets assume they come in batches
    def store(self, bin, uploadData, priority):
        cur_bin = deque([int(x) for x in str(bin)])

        trie = self.data
        while cur_bin: 
            i = cur_bin.popleft()
            print(i)
            if not trie.children[i]:
                trie.children[i] = Trie(i)
            trie = trie.children[i]

        trie.isEntry = True
        entry = trie.data
        for prop in uploadData:                                     # this will accommodate for partial data since we are iterating on the props           
            if uploadData[prop]:                                    # ensure the incoming prop is not null
                heappush(entry[prop], (priority, uploadData[prop]))
 
        # print(trie.data)

    # this will traverse the data trie and then store in an array all of the data fields, if they exist 
    # you can make a priority of which element to look at first
    def lookup(self, bin):
        res = {}
        for prop in self.props:
            res[prop] = ''
        
        cur_bin = deque([int(x) for x in str(bin)])

        trie = self.data
        while cur_bin:                          #set up the array of data streams
            cur_int = cur_bin.popleft()
            if trie.children[cur_int]:
                trie = trie.children[cur_int]
                if trie.isEntry: 
                    for prop in self.props: 
                        if trie.data[prop]:
                            res[prop] = trie.data[prop][0][1]
            else: 
                break                           # no more entries to find
        return res



# Time and Space Complexities for each Operation: 
# Store: 
# Time: O(klogn) for k letters for n elements in a colliding data store 
# Space: O(n) for each data block 

# Lookup: 
# Time: O(n*k) for a digit of length n and k length of data; 
# You'll scan the data for each digit and mark that data; and you'll replace each kth entry for more recent data so you need
# to scan each element 



        # if bin in self.data:                  # this is the old logic for non prefix
        #     entry = self.data[bin]
        #     res = {}
        #     for prop in entry: 
        #         res[prop] = entry[prop][0]
        #     return res
        # else: 
        #     return False


## Test Data

myBin = BinDB()

# bin =  123456
# priority = 1
# uploadData= {'prop1': 'Visa1', 
#              'prop2': None}
                
# myBin.store(bin, uploadData, priority)


# bin =  123456
# priority = 2
# uploadData= {'prop1': 'Visa', 
#              'prop2': 'Credit'}

# myBin.store(bin, uploadData, priority)

# print(myBin.lookup(123456))


bin =  4
priority = 2
uploadData= {'prop1': 'Visa', 
             'prop2': ''}

myBin.store(bin, uploadData, priority)

bin =  411
priority = 4
uploadData= {'prop1': '', 
             'prop2': 'credit'}

myBin.store(bin, uploadData, priority)

bin =  41
priority = 4
uploadData= {'prop1': 'Amex', 
             'prop2': 'debit'}

myBin.store(bin, uploadData, priority)


print(myBin.lookup(4111231231))