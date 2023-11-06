# trick: divide positive and evens from each other
# for a pair of numbers that are negative, the complement (i.e -1*sum of pair) must be in positive
# if you have 0's, then still x must be in negative and the complement must be in positive (and vice versa)
# the cases: 
# (1) if you have zeroes, check for all n in Neg, if -n in pos
# (2) if you have 3 zeroes, include (0,0,0)
# (3) for each combination of negs n1 and n2 = sum; check if -sum in pos
# (4) for each combination of pos p1 and p2 = sum, check if -sum in neg



## this runs: 
# Time: O(N^2)
# Space: O(N)

def threeSum(nums):
    res = set()
    pos, neg, zeroes= [], [], []
    for x in nums:
        if x > 0: pos.append(x)
        if x < 0: neg.append(x)
        if x == 0: zeroes.append(x)
    pos_check = set(pos)
    neg_check = set(neg)
    print(pos, neg, zeroes, pos_check, neg_check)
    # if 3 zeroes: add into res
    if len(zeroes) >=3:
        res.add((0,0,0))

    if len(zeroes) >0:
        for x in pos_check: 
            if -x in neg_check:
                res.add(tuple(sorted([-x, x, 0])))
    # iterate across pairs of negatives
    # if pair is negative and complement is positive and in pos_check, add
    for i in range(len(neg)):
        for j in range(i+1, len(neg)):
            comp = -1*(neg[i] + neg[j])
            if comp in pos_check: 
                res.add(tuple(sorted([neg[i], neg[j], comp])))
    # if pair is positive, and complement isnegataive and in neg_check, add
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            comp = -1*(pos[i] + pos[j])
            if comp in neg_check: 
                res.add(tuple(sorted([pos[i], pos[j], comp])))

    return res


    # # nums = sorted(nums)
    # pos = set([x for x in nums if x >=0])
    # neg = set([x for x in nums if x < 0])
    # print(pos, neg)
    # res = set()
    # for i in range(0,len(nums)-2):
    #     for j in range(i+1,len(nums)-1):
    #         tempSum = nums[i] + nums[j]
    #         triplet = tuple(sorted([nums[i], nums[j], -tempSum]))
    #         if tempSum <= 0 and -tempSum in pos:
    #             res.add(triplet) 
    #         elif tempSum > 0 and -tempSum in neg:
    #             res.add(triplet) 
    # return [list(x) for x in res]


print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([-1,0,1,1]))



#### 

def threeSum_v2(nums):

# need to sort numbers to remove duplicates for [-1, -2, 3] and [-2, -1, 3] type conditions
# create set of pos, neg, and zeroes: set (for checking membership) and array (for non-combo iteration)
# (0) if there are at least 3 zeroes, add to soln: (0,0,0)
# (1) if at least 1 zero: for x in neg, if -x in pos: add (x, -x, 0) to solution set (maintain set to take care of dupes)
# (2) then for x in neg: for y in neg, if x + y in pos: then add to solution set (x, y, -(x+y))
# (3) do the same as (2) for pos
    nums.sort()

    set_pos, set_neg, set_zero, res = set(), set(), set(), set()
    pos, neg, zero = [], [], []

    for x in nums: 
        if x > 0: 
            pos.append(x)
            set_pos.add(x)
        elif x < 0: 
            neg.append(x)
            set_neg.add(x)
        elif x == 0: 
            zero.append(x)
            set_zero.add(x)

    print(neg, pos)        
    if set_zero: 
        if len(zero) >= 3:
            res.add((0,0,0))
        for x in pos: 
            if -x in set_neg: 
                res.add((-x, 0, x))
    for i in range(len(neg)):
        for j in range(i + 1, len(neg)):
            if -(neg[i] + neg[j]) in set_pos: 
                res.add((neg[i], neg[j], -(neg[i] + neg[j])))
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            if -(pos[i] + pos[j]) in set_neg: 
                res.add((-(pos[i] + pos[j]), pos[i], pos[j]))
    return res

print(threeSum_v2([-1,0,1,2,-1,-4]))

print(threeSum_v2([1,1,-2]))