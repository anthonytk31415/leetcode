# two pointers! 

#time: O(n)
#space: O(1)

# proof: 
# - If you start with i = 0, j = len(height)-1, this maximizes the width of the rectangle.
#   All other rectangles will be smaller width so you have to increase height.
# - at each iteration, we'll always maintain the largest of the two heights. In order for the
#   height to increase, you must get a larger height. So smaller heights can be safely thrown away.
# - we'll iterate until i >= j. 


from math import inf

def maxAreaBF(height):
    maxArea = -inf
    coords = None
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = min(height[i], height[j])*(j-i)
            print(area)
            if maxArea < area: 
                maxArea = area
                coords = (i,j) 
    return maxArea, coords



# 32
# height[i] < height[j]:
# traverse back i if i-1 >=0 
# 
def maxArea(height):
    i, j = 0, len(height) - 1
    maxWater = -inf
    while i < j: 
        maxWater = max(maxWater, min(height[i], height[j])*(j-i))
        if height[i] < height[j]:
            i +=1
        else: 
            j -=1
    return maxWater

# height = [1,1]

# height = [5,3,9,4,7,6,8,1,2]

height = [2,3,4,5,18,17,6]

print(maxArea(height))