class Solution {
    func isMonotonic(_ nums: [Int]) -> Bool {
        if nums.count <= 2 {
            return true
        }
        
        var set_inc = false 
        var inc = false
        
        for i in 1..<nums.count{
            // set the direction of monotonicity 
            if set_inc == false {
                if nums[i-1] < nums[i] {
                    inc = true 
                    set_inc = true
                } else if nums[i-1] > nums[i] {
                    inc = false
                    set_inc = true
                }
            }

            // increasing, and we meet decreasing indexes
            if set_inc == true && inc == true && nums[i-1] > nums[i] {
                return false
            }
            // decreasing, and we meet increasing indexes 
            if set_inc == true && inc == false && nums[i-1] < nums[i] {
                return false
            } 
        }
        return true 
    }
}

// let nums = [6,5,4,4]
let nums = [1,3,2]
let s = Solution()
print(s.isMonotonic(nums))
