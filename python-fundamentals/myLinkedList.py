# myLinkedList


class MyLinkedList:

    class ListNode: 
        def __init__(self, val, next=None, prev=None):
            self.val = val
            self.next = next
    
    def __init__(self):
        self.head = None   
        self.length = 0

    def seek(self, index: int) -> int:
        if self.length == 0 or not (0 <= index < self.length): 
            return -1
        
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def get(self, index: int) -> int:
        node = self.seek(index)
        if node == -1: return -1
        return node.val
        

    def addAtHead(self, val: int) -> None:
        newNode = self.ListNode(val, next=self.head)
        self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addAtHead(val)
            return 

        tail = self.seek(self.length - 1)
        tail.next = self.ListNode(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length: return 
        if index == 0: 
            self.addAtHead(val)
            return 
        if index == self.length: 
            self.addAtTail(val)
            return 
        prev = self.seek(index - 1)
        next = prev.next
        newNode = self.ListNode(val)
        prev.next =  newNode
        newNode.next = next
        self.length += 1
        return 
    

    def deleteAtIndex(self, index: int) -> None:
        if not (0 <= index < self.length): return 
        if index == 0: 
            newHead = self.head.next
            self.head = newHead
        elif index == self.length - 1:
            prev = self.seek(self.length - 2)
            prev.next = None
        else: 
            prev = self.seek(index - 1)
            newNext = prev.next.next
            prev.next = newNext
    
        self.length -=1
        return 




z = MyLinkedList()
z.addAtHead(4)
z.get(1)
z.addAtHead(1)
z.addAtHead(5)
z.deleteAtIndex(3)
z.addAtHead(7)
z.get(3)
z.get(3)
z.get(3)
z.addAtHead(1)
z.deleteAtIndex(4)
z.addAtHead(1)
# print(z.length)
# print(z.head.val)


# z.addAtTail(3)
# z.addAtIndex(1,2)




["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
[[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]