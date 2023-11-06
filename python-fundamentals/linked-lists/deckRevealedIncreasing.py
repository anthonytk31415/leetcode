from collections import deque
# Time: O(nlogn)
# Space: O(n)

def deckRevealedIncreasing(deck):

    ## go through the algo to create the order
    deck.sort()
    order = deque([i for i in range(len(deck))])
    idx_order = []
    while order:
        cur = order.popleft()
        idx_order.append(cur)
        if order:
            go_back = order.popleft()
            order.append(go_back)
    res = [None]*len(deck)
    for i in range(len(deck)):
        res[idx_order[i]] = deck[i]
    return res

# then sort the deck 
# then assign the new array by the idx_order
deck = [0,2,4,6,3,1,5]
# deck = [17,13,11,2,3,5,7]
print(deckRevealedIncreasing(deck))




# #       [0,1,2,3,4,5,6] >> [0,2,4,6,3,1,5]
# # rank: [0,5,1,4,2,6,3] 

# [0, 5, 1, 4, 2, 6, 3]

# 01234
# 456