def PredictTheWinner(nums):
    memo = {}               # (nums, turn, score1, score2) : True/False

    def helper(nums, turn, score1, score2, memo):
        if (tuple(nums), turn, score1, score2) in memo: 
            return memo[(tuple(nums), turn, score1, score2)]
        else: 
            res = None
            if not nums: 
                res = score1 >= score2
            else: 
                if turn: 
                    res = helper(nums[1:], not turn, score1 + nums[0], score2, memo) or  helper(nums[:-1], not turn, score1  + nums[-1], score2, memo) 
                elif not turn: 
                    res = helper(nums[1:], not turn, score1, score2 + nums[0], memo) and  helper(nums[:-1], not turn, score1, score2 + nums[-1], memo) 
            memo[(tuple(nums), turn, score1, score2)] = res
            return res
        
    return helper(nums, True, 0, 0, memo)
        
nums = [1,5,2]
# nums = [1,5,233,7]
print(PredictTheWinner(nums))