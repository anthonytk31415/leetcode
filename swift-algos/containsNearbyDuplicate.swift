func containsNearbyDuplicate1(_ nums: [Int], _ k: Int) -> Bool {
    var lookup: [Int: Int] = [:]
    for (i, num) in nums.enumerated() {
        if let check: Int = lookup[num],  abs(check - i) <= k {
            return true
        }
        lookup[num] = i
    }
    return false
}



// func containsNearbyDuplicate(_ nums: [Int], _ k: Int) -> Bool {
//     var dict = [Int: Int]()
//     for (currentIndex, num) in nums.enumerated() {
//         if let duplicateIndex = dict[num], currentIndex - duplicateIndex <= k {
//             return true
//         }
//         dict[num] = currentIndex
//     }
//     return false
// }

// let nums = [1,2,3,1,2,3]
// // print(abs(-1))
// print(containsNearbyDuplicate(nums, 2))