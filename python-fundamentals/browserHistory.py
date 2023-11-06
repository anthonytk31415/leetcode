

# this was a success!
# the trick is doubly linked list

# instantiate: 
# - head is the home page. it is never removed.
# - # implement a head and a tail
# have a current pointer that points wher eyou are currently

# visit: 
# - new visits puts the current.next = new visit and current = new visit node; 
# - visit also points to tail and vice versa
# - this mechanism also cuts off forwards 

# back and forward function similarly; 
# just move the cur pointer to the prev or to the next if its not head or tail. 
# if it is head or tail, then just do nothing 



class DoubleLinkedList:
    def __init__(self, url=None):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = DoubleLinkedList(homepage)
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cur = self.head

    def visit(self, url: str) -> None:
        newNode = DoubleLinkedList(url)

        self.cur.next = newNode
        newNode.prev = self.cur

        self.tail.prev = newNode
        newNode.next = self.tail

        self.cur = newNode        

    def back(self, steps: int) -> str:
        def back_helper(self):
            if self.cur.prev != None: 
                self.cur = self.cur.prev
        for _ in range(steps):
            back_helper(self)
        return self.cur.url

    def forward(self, steps: int) -> str:
        def forward_helper(self):
            if self.cur.next.next != None: 
                self.cur = self.cur.next
        for _ in range(steps):
            forward_helper(self)
        return self.cur.url