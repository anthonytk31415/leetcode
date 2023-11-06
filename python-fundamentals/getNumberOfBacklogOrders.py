from heapq import heappush, heappop


def getNumberOfBacklogOrders(orders):
    buys, sells = [], []                         # maintain a max_heap for buys; maintain a min_heap for sells

    for cur_price, cur_amt, cur_type in orders: 
        # for buys - find the cheapest sell where buy >= sell; pop sells to find the cheapest sell 
        if not cur_type:
            while cur_amt >0 and sells and cur_price >= sells[0][0]:
                cs = heappop(sells)
                cs_price, cs_amt = cs                   # case when cur_amt decreases and current
                if cur_amt > cs_amt:                    # sell block is exhausted with amt  
                    cur_amt = cur_amt - cs_amt
                else: 
                    cs_amt = cs_amt - cur_amt           # case when cur_amt > 0 and current sell block 
                    cur_amt = 0                         # still has amt -> push back the diff to the min_heap
                    heappush(sells, (cs_price, cs_amt)) 
            if cur_amt >0:                              # after examining sells, push the remaining 
                heappush(buys, (-cur_price, cur_amt))   # buy order into the max_heap

        # for sells - find the most expensive buy where sell <= buy; pop buys to find the most expensive buy
        else:
            while cur_amt >0 and buys and cur_price <= -buys[0][0]: 
                cb = heappop(buys)
                cb_price, cb_amt = cb                     
                cb_price = -cb_price
                if cur_amt > cb_amt:                    # case when cur_amt decreases and 
                    cur_amt = cur_amt - cb_amt          # current sell block is exhausted with amt  
                else: 
                    cb_amt = cb_amt - cur_amt           # case when cur_amt > 0 and current sell block still
                    cur_amt = 0                         # has amt -> push back the diff to the min_heap
                    heappush(buys, (-cb_price, cb_amt))

            if cur_amt >0:                              # after examining sells, push the 
                heappush(sells, (cur_price, cur_amt))   # remaining buy order into the max_heap

    return sum([x1 for (x0, x1) in buys] + [x1 for (x0, x1) in sells]) % (10**9 + 7)


## test cases

# orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
orders = [[26,7,0],[16,1,1],[14,20,0],[23,15,1],[24,26,0],[19,4,1],[1,1,0]]
# orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
print(getNumberOfBacklogOrders(orders))