

# Intuition: Given some height, what is the max valid width that is a candidate? It's where we hit closest heights on our right and left that are less than the current height. 
# 

# We iterate across each i in heights. Each i can form a rectangle as big as its height and the two heights smaller than itself. 
# So we keep a monotonic increasing stack:
# - before we append the current height to the stack, we'll pop previous heights that are larger than the current height. This way
# - we maintain the increasing stack. 
# - We see that the element behing the current one int he stack will be smaller and hence its index will always be the leftmost boundary
# - (since its a monotonic stack, the larger elements between the element behind the current one in the stack 
#   and the current one in the stack would be larger and would form valid heights for the rectangle
# - the rightmost boundary will be the current i since we're looking the situation where the current element's height < stack[-1]
# keep an monotonically increasing stack so that the length of a rectangle will be the length of the previous element in the stack
# the 

def largestRectangleArea(heights):
    heights.append(0) # append 0 allows you to give the min height the max width of the entire heights array. Same with the -1 in stack.
    incStack = [-1]

    maxRect = -inf
    for i, curHeight in enumerate(heights):
        while incStack and curHeight < heights[incStack[-1]]:
            height = heights[incStack.pop()]
            width = i - incStack[-1] - 1
            maxRect = max(maxRect, height*width)
        incStack.append(i)
    heights.pop()
    return maxRect

heights = [2,1,5,6,2,3]
heights = [0]
print(largestRectangleArea(heights))