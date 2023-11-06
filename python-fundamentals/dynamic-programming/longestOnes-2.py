# longestOnes-2.py


def countOneZero(nums):
    res = []
    cur_streak = None
    cur_val = None
    
    for i, x in enumerate(nums):
        if i == 0: 
            cur_streak = 1
            cur_val = x
        else: 
            if cur_val == x: 
                cur_streak +=1
            else: 
                res.append((cur_val, cur_streak))
                cur_streak = 1
                cur_val = x
    res.append((cur_val, cur_streak))
    return res


# print(countOneZero(nums))

## res[i] = (one or zero; number of consecutives)

def longestOnes(nums, k):
    memo = {} # key = (string, k); value = max number of consecutive 
    nums = countOneZero(nums)

    def helper(nums, k, pred, memo, extraZeroes):
        if (tuple(nums), k, pred, extraZeroes) in memo: 
            return memo[(tuple(nums), k, pred, extraZeroes)]
        else: 
            res = []
            if not nums:
                ones_to_add = 0
                if k > 0: 
                    ones_to_add = min(k, extraZeroes)
                res.append(pred + ones_to_add)
            else: 
                char, count_char = nums[0] 
                if char == 0:
                    if k == 0: 
                        res.append(pred)
                        res.append(helper(nums[1:], k, 0, memo, min(extraZeroes + count_char, k)))
                    else: 
                        #break the chain with 0
                        res.append(helper(nums[1:], k, 0, memo, count_char-1))
                        if k >= count_char:                       #continue the chain
                            res.append(helper(nums[1:], k - count_char, count_char + pred, memo, min(k, extraZeroes)))
                else: 
                    res.append(helper(nums[1:], k, pred + count_char, memo, min(k, extraZeroes)))
            res = max(res)
            memo[(tuple(nums), k, pred, extraZeroes)] = res
            return res
    ulti = helper(nums, k, 0, memo, 0)
    # print(memo)
    return ulti


# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2

# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
# nums = [0,0,1,1,1,0,0]
# k = 0
# 3


nums = [1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1]
k = 144

# print(sum(nums))
# print(len(nums))
print(longestOnes(nums, k))