


def minCost(colors, neededTime):
    left = 0
    right = 1
    res = 0
    skipped = set()
    while right < len(colors):
        # print(left, right)
        while left in skipped: left += 1        
        if colors[left] == colors[right]:

            if neededTime[left] <= neededTime[right]:
                res += neededTime[left]
                skipped.add(left)
                left += 1
            else: 
                res += neededTime[right]
                skipped.add(right)
        else: 
            left += 1
        right += 1

    # print(left, right, skipped)
    return res

# colors = "abaac"
# neededTime = [1,2,3,4,5]

# colors = "aabaa"
# neededTime = [1,2,3,4,1]

# colors = "aaaaaaaa"
# neededTime = [1,3,6,5,5, 10, 6, 6]

colors = "aaaaaaaaaaaaaa"

neededTime = [1,3,6,5,4,5,4,4,2,8,3,10,6,6]

print(minCost(colors, neededTime))