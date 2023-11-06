class Solution {
    func createTargetArray(_ nums: [Int], _ index: [Int]) -> [Int] {
        var target = [Int]()
            for i in 0..<nums.count{
                let idx = index[i]
                let num = nums[i] 
                if idx < target.count && 0 <= idx {
                    target.insert(num, at: idx)
                } else {
                    target.append(num)
                }
                print(target)
            }
        return target
    }
}


let nums = [0,1,2,3,4]
let index = [0,1,2,2,1]
let s = Solution()
print(s.createTargetArray(nums, index))