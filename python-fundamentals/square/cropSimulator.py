cropData = [
{"name": "Cauliflower", "seed_cost": 80, "sell": 175,"grow": 6}, 
{"name": "Garlic","seed_cost": 40, "sell": 60, "grow": 6}, 
{"name": "Kale", "seed_cost": 70, "sell": 110, "grow": 3}, 
{"name": "Turnip", "seed_cost": 20, "sell": 35, "grow": 2} 
]


# write (profit, data), put in max heap, then while you still have money, "process"
from heapq import heappush, heappop


# Time: O(nlogn) for putting n items in the maxHeap; everything else runs in linear time
# space O(n) for n crops

def purchaseFn(cash):
    maxHeap = []

    for crop in cropData: 
        cur_profit = (crop['sell'] - crop['seed_cost'])/crop['grow']
        heappush(maxHeap, (-cur_profit, crop))
    
    crops_purchased = []

    while cash > 0 and maxHeap: 
        cur_profit, curCrop = maxHeap[0]
        if cash >= curCrop['seed_cost']:
            cash = cash - curCrop['seed_cost']
            crops_purchased.append(curCrop['name'])
        else: 
            heappop(maxHeap)


    print(f'{cash} remaining money')
    return crops_purchased


# print(purchaseFn(105))



def purchaseMoneyDays(cash, days_left):
    maxHeap = []

    for crop in cropData: 
        cur_profit = (crop['sell'] - crop['seed_cost'])/crop['grow']
        heappush(maxHeap, (-cur_profit, crop))
    
    crops_purchased = []
    # print(maxHeap)
    while cash > 0 and maxHeap: 
        cur_profit, curCrop = maxHeap[0]
        if cash >= curCrop['seed_cost'] and curCrop['grow']<= days_left:
            cash = cash - curCrop['seed_cost']
            crops_purchased.append((curCrop['name'], curCrop['sell'], curCrop['grow']))
        else: 
            heappop(maxHeap)


    # print(f'{cash} remaining money')
    return crops_purchased, cash


print(purchaseMoneyDays(105, 3))

# modify the purchase fn so that you only buy things that are within the time limit 
# 


def plantCycle(cash, days):
    inventory = []              ## min heap; we will throw things here so that when we pull out we're always pulling out the smallest days 

    cur_day = 0
    while cur_day <= days: 
        days_left = days - cur_day 
        print('cur_day:', cur_day, 'cash:', cash, 'inventory:', inventory, 'days_left:', days_left)
        
        ## harvest crops if you can 
        
        while inventory and inventory[0][0] == cur_day:
            cropHarvestDay, cropSell = heappop(inventory)
            cash += cropSell 
        
        print('before buying cash day:', cur_day, 'cash:', cash, 'days_left:', days_left)
        ## buy crops if you can 
        crops_purchased, cash = purchaseMoneyDays(cash, days_left)
        for crop in crops_purchased:
            cropName, cropSell, cropGrow = crop
            heappush(inventory, (cropGrow + cur_day, cropSell))

        print('end day:', cur_day, 'cash:', cash)
        cur_day +=1
    return cash 

print(plantCycle(60, 5))