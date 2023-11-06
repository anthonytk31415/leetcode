# pathsum3

# 5
# 5+4 4
# 5+4+11, 4+11, 11, 

# worst case: O(n); best case for balanced tree: O()
# space: worst case: O(n)

## for a balanced tree: 
# height = 1: 
# tracker = []; len = 1

# height = 2: 
# tracker len = 2

# height = 3
# tracker len = 3
# height = 4 

# height = 4
# tracker len = 4

# height = log(n)
# tracker = log(n)






# def pathsum(root, targetSum):
#     def helper(root, targetSum, tracker):
#         if root: 
#             tracker = [(x + root.val) for x in tracker]
#             tracker.append(root.val)
#             counter = 0 
#             for x in tracker: 
#                 if x == targetSum:
#                     counter +=1
#             return counter + helper(root.left, targetSum, tracker) + helper(root.right, targetSum, tracker)
#         else: 
#             return 0
#     return helper(root, targetSum, [])



def pathsum(root, targetSum):
    def helper(root, targetSum, tracker):
        if root: 
            tracker = [(x + root.val) for x in tracker]
            tracker.append(root.val)
            counter = 0 
            for x in tracker: 
                if x == targetSum:
                    counter +=1
            return counter + helper(root.left, targetSum, tracker) + helper(root.right, targetSum, tracker)
        else: 
            return 0
    return helper(root, targetSum, [])