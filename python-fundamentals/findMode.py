

from collections import defaultdict

# Time O(n) result; traversing the tree only once and keeping track of the
# Space: O(n); keeping track of max as you go along as well as frequency of values 

def findMode(root):
    stats = [0, set()] ## stats[0] = cur_count, stats[1] = set of values
    track = defaultdict(int) ## value: count
    def helper(root, track, stats):
        if not root: 
            return 
        else: 
            track[root.val] +=1
            if track[root.val] == stats[0]:
                stats[1].add(root.val)
            elif track[root.val] > stats[0]:
                stats[0] = track[root.val]
                stats[1] = set()
                stats[1].add(root.val)
            helper(root.left, track, stats)
            helper(root.right, track, stats)

    helper(root, track, stats)
    return list(stats[1])