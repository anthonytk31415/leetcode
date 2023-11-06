# find the min path for each row for each column starting at the top of the triangle to the bot
# memo that path. 
# return the min of the last row

# time: O(n) --> traverse through each element in the triangle
# space: O(1); we'll use the exisitng triangle to keep the min path for each row/col pair

from collections import defaultdict

def minimumTotal(triangle):

    for row in range(1, len(triangle)):        
        for col in range(len(triangle[row])):
            if col == 0: 
                triangle[row][col] = triangle[row-1][0] + triangle[row][col]
            elif col == len(triangle[row]-1):
                triangle[row][col] = triangle[row-1][col-1] + triangle[row][col]
            else: 
                triangle[row][col] = triangle[row][col] + min(triangle[row-1][col-1], triangle[row-1][col])
    
    return min(triangle[-1])