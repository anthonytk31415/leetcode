# def rotate1(nums, k):
#     k = k % len(nums)
#     newNums = nums[-k:] + nums[:-k]
#     for i in range(len(nums)):
#         nums[i] = newNums[i]




# Heres a solution that does so in place with O(1) space O(n) Time. 
# Concept is that we start at 0 and then put it at the 0 +kth slot and then put the kth element at the len(nums) mod (k + kth) and so forth
# but note that we'll hit a cycle if the gcd of len(nums) and k > 1. So we ahve to go through gcd rotations where we start at i = 0, 1, ... rotations - 1
# and then for each rotation, we'll play slot hopping len(nums)/rotations times 
# This is kind of a group theory type problem  


def rotate(nums, k):
    def gcd(a, b): 
        while b: 
            a, b = b, a % b
    return a

    k = k % len(nums)

    rotations = int(gcd(len(nums), k))
    cycleLength = int(len(nums) / rotations)

    r = 0
    i = -1
    print(rotations, cycleLength)
    while r < rotations:
        i += 1
        sub = nums[i]

        for _ in range(cycleLength):
            idx = (i + k) % len(nums)
            holder = nums[idx]
            nums[idx] = sub
            sub = holder
            i = idx
        r += 1


# nums = [1,2,3,4,5,6,7]
# k = 3

# nums = [1,2]
# k = 1
# nums = [1,2,3,4,5,6,7,8,9]
# k = 3

nums = [1,2,3,4,5,6,7,8,9,10,11,12]
k = 8

# nums = [-1,-100,3,99]
# k = 2
print(rotate(nums, k))
print(nums)

print(gcd(12, 5))


