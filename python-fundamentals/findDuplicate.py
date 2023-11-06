# def findDuplicate(nums):
#     lookup = set()
#     for x in nums: 
#         if x not in lookup: 
#             lookup.add(x)
#         elif x in lookup: 
#             return x




# tortoise and hare solution: 
# O(n) time, O(1) space

def findDuplicate(nums):
    t = h = nums[0]
    # find intersection point
    while True:
        t = nums[t]
        h = nums[nums[h]]
        if t == h: 
            break
    # then find the entry point
    t = nums[0]
    while t != h: 
        t = nums[t]
        h = nums[h]
    return h

print(findDuplicate([1,3,4,2,2]))