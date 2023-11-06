# Time: O(n) solution; 
# Space: O(1) 
# two pointers with some fancy tracking 
# trick: keep track of the minimum of s1 of s2: 

# Keep the smallest s1 and s2 to "Make it easier" to find a 3 linked chain
# for s1: 
# (populate s2: ) if cur > s1
# ** if cur < s2: --> s2 = cur
# ** if cur > s2 --> True
# if cur < s1:  s1 = cur1

def increasingTriplet(nums):
    if not nums: 
        return False

    s1 = nums[0]
    s2 = None

    for i in range(1, len(nums)):
        # print(f's1 = {s1}, s2={s2}; i = {nums[i]}')
        if nums[i] > s1: 
            if s2 == None:
                s2 = nums[i]
            else: 
                if s2 > nums[i]:
                    s2 = nums[i]
                elif nums[i] > s2: 
                    return True
        elif nums[i] < s1: 
            s1 = nums[i]
    return False

x = [5,4,3,2,1]
# x = [9, 10, 1, 2, 3]
# x = [9,15,1,3,2,14]
print(increasingTriplet(x))