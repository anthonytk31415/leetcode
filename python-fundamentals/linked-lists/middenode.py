# middlenode

def middlenode(head):
    oneStep = head.next
    if oneStep==None:
        return head
    twoStep = head.next.next
    while twoStep:
        if twoStep.next == None:
            return oneStep  
        else: 
            twoStep = twoStep.next.next
            oneStep = oneStep.next     
    return oneStep