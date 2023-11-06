func summaryRanges(_ nums: [Int]) -> [String] {
    if nums.count == 0 { 
        return []
    }

    if nums.count == 1 { 
        return ["\(nums[0])"]
    }


    var res = [String]()
    var chain = false 
    var startChain = nums[0]
    var endChain: Int? = nil

    for i in 1..<nums.count {
        // starts a chain
        if !chain && nums[i] == startChain + 1 {
            chain = true
            endChain = nums[i]
        } else if !chain && nums[i] != startChain + 1 {
        // single element, new single element
            chain = false
            res.append("\(startChain)")
            startChain = nums[i]
            endChain = nil
        } else if chain && nums[i] != endChain! + 1 {
        // was a chain, chain breaks
            chain = false 
            res.append("\(startChain)->\(endChain!)")
            startChain = nums[i]
            endChain = nil 
        } else if chain && nums[i] == endChain! + 1 {
        // was a chain, continue chain
            endChain = nums[i]
        }
    }

    if chain {
        res.append("\(startChain)->\(endChain!)")
    } else {
        res.append("\(startChain)")
    }
    return res 
    // at the end, append the last element: single element or chain
}
var nums = [0,1,2,4,5,7]
// var nums = [0,2,3,4,6,8,9]
print(summaryRanges(nums))