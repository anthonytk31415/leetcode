// create a hash table that contains the number and then a list of the index; for dupes, 
// the last index will contain the last one
// 

// then for each num in nums, find if its "complement" exists and record the longest length


class Solution {
    func findLHS(_ nums: [Int]) -> Int {
        var tracker = [Int: Int]()
        for x in nums{
            if tracker[x] != nil {
                tracker[x]!+=1
            } else {
                tracker[x]=1
            }
        }
        var res = 0
        for x in nums{
            for y in [x + 1, x - 1]{
                if tracker[y] != nil{
                    res = max(res, tracker[y]! + tracker[x]!)
                }
            }
        }

        return res
    }
}

// let nums = [1,3,2,2,5,2,3,7]
let nums = [1,2,3,4]
let s = Solution()
print(s.findLHS(nums))