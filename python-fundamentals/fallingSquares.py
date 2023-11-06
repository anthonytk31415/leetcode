# falling squares

# if a square falls, it it inherits the height of the first highest prior square 
# if the square hits another square, then the prior square "loses" 

## is this n log n? 


from heapq import heappush, heappop

# x1, x2; y1, y2
def isOverlap(block1, block2):
    x1, x2 = block1
    y1, y2 = block2
    if x1 <= x2 <= y1 <= y2: return False
    if y1 <= y2 <= x1 <= x2: return False
    return x2 > y1 or y2 > x1

# for each position, check if it overlaps with anything in Order (in descending height order). 
# If it does, 
# height_new = height_cur + height_position
# res = append(height_new)
# if Not: 
# now heappush everything back in

def fallingSquares(positions):
    order = []      # blocks will be sorted by height
    checked = []
    res = []
    for x1, height_x in positions: 
        x2 = x1 + height_x
        print(x1, x2, height_x)
        while order: 
            height_y, y1, y2 = heappop(order)
            height_y = -height_y
            checked.append((height_y, y1, y2))
            if isOverlap((x1, x2), (y1, y2)):
                print('overlap: ', (x1, x2), (y1, y2))
                height_x = height_x + height_y
                break 
            
        while checked: 
            height_z, z1, z2 = checked.pop()
            heappush(order, (-height_z, z1, z2,))
        
        heappush(order, (-height_x, x1, x2,))
        res.append(-order[0][0])
        print(order, checked)
    return res

# positions = [[1,2],[2,3],[6,1]]
# Output: [2,5,5]
# positions = [[100,100],[200,100]]
positions = [[6,1],[9,2],[2,4]]
# >> 1,2,4
print(fallingSquares(positions))