from collections import defaultdict

# Sliding window technique
# - our window will ahve: left, middle, right
# - left to right will be the largest window with k distinct 
# - our invariants: when window is valid: 
#     - mid to right will be the smallest window (up to right)
#     - left to right will be the largest window (up to right)
#     - we add to our res: mid - left + 1: logic is we start from smallest window (1) and then we have delta (mid - left) more variants with k distinct integers

# O(n) Time and O(n) Spce

def subarraysWithKDistinct(nums, k):

    left, mid, res = 0, 0, 0
    countLongest = defaultdict(int)
    countShortest = defaultdict(int)
    for right, rnum in enumerate(nums):
        countLongest[rnum] += 1        
        countShortest[rnum] += 1
        
        # when count > k, we'll push left and remove ints from countLongest and countShortest
        # Note: when left == mid, we carry them forward and together  
        while len(countLongest) > k and len(countShortest) > k and left + 1 < len(nums):
            countLongest[nums[left]] -= 1
            if countLongest[nums[left]] == 0: del countLongest[nums[left]]
            if left == mid: 
                countShortest[nums[mid]] -= 1
                if countShortest[nums[mid]] == 0: del countShortest[nums[mid]]
                mid += 1
            left += 1

        if len(countLongest) == k:
            # find the shortest (mid): if the count of the next mid pushes shortest < k: then stop
            while len(countShortest) >= k and countShortest[nums[mid]] > 1: 
                countShortest[nums[mid]] -= 1
                if countShortest[nums[mid]] == 0: del countShortest[nums[mid]]
                mid += 1
            res += mid - left + 1

    return res


nums = [1,2,1,2,1,3] 
k = 2
print(subarraysWithKDistinct(nums, k))