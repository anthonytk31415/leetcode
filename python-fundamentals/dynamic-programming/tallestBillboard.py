# here's a good problem on how you would choose the best set

def tallestBillboard(rods):
    # dp[diff] = sharedSum represents for a given a, b (sum of two sets of #s), assume a - b = diff, dp is the largest sharedSum 
    # for a given diff. We will return dp[0], the largest sharedSum among a and b whose diff = 0. 
    dp = {0:0}      # instantiate with largest 
    for rod in rods: 
        dp_items = [(diff, sharedSum) for diff, sharedSum in dp.items()]
        for diff, sharedSum in dp_items:                                 
            # add to the larger side
            dp[diff + rod] = max(dp.get(diff + rod, 0), sharedSum)        # get the larger of the prior "diff's" common sum, or the diff's sharedSum 
            # add to the smaller side
            dp[abs(diff - rod)] = max(dp.get(abs(diff - rod), 0), sharedSum + min(diff, rod))   # shared sum increases by diff (if rod is bigger) or rod (if diff is bigger); we choose abs(diff - rod) to handle diff > rod or diff < rod

    # one of these combinations will have a diff = 0, or that diff is zero
    return dp[0]

rods = [1,2,3,4,5,6]
print(tallestBillboard(rods))


