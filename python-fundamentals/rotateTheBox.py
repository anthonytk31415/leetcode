
# first rotate the box; 
# then for each column, and for each 
# then start at the bottom; 
#   keep track of the lowest point; 
#   if it's a stone, move it to the lowest point; then shift the lowest point 1 + old 
#   # if it's an obstacle, lowest point = 1 + old 
#   #  
def rotateTheBox(box):
    
    res = [[None for _ in range(len(box))] for _ in range(len(box[0]))]
    # rotate the box 90'
    for i in range(len(box)):
        for j in range(len(box[0])):
            res[j][len(res[0]) -1 - i] = box[i][j]

    # now do the dp logic 
    for j in range(len(res[0])):
        bottom = len(res) - 1
        for i in range(len(res) - 1, -1, -1):
            print(i, j, res[i][j], bottom)
            if res[i][j] == '#':
                res[i][j] = '.'
                res[bottom][j] = '#'
                bottom -=1
            elif res[i][j] == '*':
                bottom = i - 1

    return res


box = [["#",".","*","."],
       ["#","#","*","."]]

print(rotateTheBox(box))