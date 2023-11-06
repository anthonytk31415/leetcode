# search

def search(nums, target):
    def helper(nums, target, p, r):
        # print(f'{p}, {r}')
        if r - p < 0:
            return -1
        elif r-p == 0:
            if nums[p] == target:
                return p
            else: 
                return -1
        q = ((r-p)// 2) + p
        if nums[q] == target:
            return q
        elif target < nums[q]:
            return helper(nums, target, p,q-1) 
        else: 
            return helper(nums, target, q+1, r)
    return helper(nums, target, 0, len(nums)-1)

# a = [-1,0,3,5,9,12]
# a = [-1,0,3,5,9,12, 23, 25, 26, 27, 28, 44, 444, 2342, 2343242]
# a = [5]

a = [2,5]
print(search( a, 99))

# [5]

# 0,1,2,3,4,5
# length = 6

# 0,1,2,3,4,5,6,7,8,9; len = 10
# 0-4, 5-9

# len // 2 = 5

# q = 3 = (len(nums)) // 2

# def search(self, nums, target):
#     q = (len(nums)) // 2
#     if nums[q] == target:
#         return q
#     else:
#         if target < nums[q]:
#             return self.search(nums[:q], target) 
#         else: 
#             return self.search(nums[q:], target)
    