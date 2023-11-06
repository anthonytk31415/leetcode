
# Time: O(N); you're running through each node 2*n times with constant time lookup
# Spce: O(N) for constant time lookup 

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    
def copyRandomList(head):

    orig = {}           # key = node; val = index
    new = {}            # key = index; val = node
    dummy = Node(0)     # build the new node
    i = 0
    cur_old  = head     # will reference current in orig
    cur_new = dummy     # will reference right before current in orig
    while cur_old: 
        orig[cur_old] = i
        cur_new.next = Node(cur_old.val)
        cur_old = cur_old.next
        cur_new = cur_new.next
        new[i] = cur_new
        i +=1

    #now do the randoms after dicts are built
    cur_old = head
    while cur_old: 
        index_cur = orig[cur_old]
        if cur_old.random != None: 
            index_random = orig[cur_old.random]
            new[index_cur].random = new[index_random]
        cur_old = cur_old.next
    return dummy.next


## review the O(1) technique 
# https://leetcode.com/problems/copy-list-with-random-pointer/solutions/43632/java-very-simple-and-clean-solution-with-o-n-time-o-1-space-with-algorithm/?orderBy=most_votes&page=2