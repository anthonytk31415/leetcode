
from collections import defaultdict

# x = defaultdict(int)
# x[0] += 1
# print(x)

def subarraysWithKDistinct(nums, k):

    left = 0
    mid = 0
    countLongest = defaultdict(int)
    countShortest = defaultdict(int)
    res = 0
    # print(res, "start")
    for right, rnum in enumerate(nums):
        countLongest[rnum] += 1        
        countShortest[rnum] += 1
        
        # how to adjust left: generally, that is when longest > k: push left forward 
        while len(countLongest) > k and len(countShortest) > k and left + 1 < len(nums):
            countLongest[nums[left]] -= 1
            if countLongest[nums[left]] == 0: del countLongest[nums[left]]
            if left == mid: 
                countShortest[nums[mid]] -= 1
                if countShortest[nums[mid]] == 0: del countShortest[nums[mid]]
                mid += 1
            left += 1
            # print("shortest: {} , longest: {} , left {}, middle {},  right {}".format(countShortest, countLongest, left, mid, right))

        # we equal k; and next one will bring us greater than k; we found longest interval
        if len(countLongest) == k :
            # print("shortest: {} , longest: {} , left {}, middle {},  right {}, added to res: {}".format(countShortest, countLongest, left, mid, right, mid - left + 1))
            # find the shortest: if the count of the next mid pushes shorest < k: then stop
            while len(countShortest) >= k and countShortest[nums[mid]] > 1: 
                countShortest[nums[mid]] -= 1
                if countShortest[nums[mid]] == 0: del countShortest[nums[mid]]
                mid += 1
            # print("initiating add", "shortest: {} , longest: {} , left {}, middle {},  right {}, added to res: {}".format(countShortest, countLongest, left, mid, right, mid - left + 1))
            res += mid - left + 1

    return res


nums = [1,2,1,2,1,3] 
# nums = [1,2,1,2,3]
k = 2
print(subarraysWithKDistinct(nums, k))