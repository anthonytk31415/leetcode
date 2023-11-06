func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var lookup: [Int : Int] = [:]
    for (idx, val) in nums.enumerated() {        
        if let cur: Int = lookup[target - val] {
            return [idx, cur]
        } else {
            lookup[val] = idx
        }
    }
    return []
}



// func twoSum2(_ nums: [Int], _ target: Int) -> [Int] {
//     var map = [Int: Int]()
//     for (i, n) in nums.enumerated() {
//         let diff = target - n
//         if let j = map[diff] {
//             return [i, j]
//         }
//         map[n] = i
//     }
//     return []
// }

// var lookup: [Int: Int] = [1:2, 3:4, 5:6]

// let z: Bool = lookup[8] != nil

// print(z)




// var map = [Int: Int]()
// var map: [Int: Int] = [:]

