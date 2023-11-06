import Foundation

func minSpeedOnTime(_ dist: [Int], _ hour: Double) -> Int {
    if dist.count > Int(ceil(hour)) {
        return -1
    }

    var left = 1
    let remainder = hour - Double((dist.count - 1))


    let right_1: Int = (dist.count - 1) + Int(ceil(Double(dist[dist.count - 1])/remainder))
    var right: Int = max(right_1, dist.max(by: {$0 < $1}) ?? dist[0])
    // print(left, right)
    while left <= right {
        let mid = Int(floor((Double(left) + Double(right))/2))
        // print(left, right, mid)
        var totalTime: Double = 0
        if dist.count - 2 >= 0 {
            for i: Int in 0 ... dist.count - 2 {
                totalTime += ceil(Double(dist[i])/Double(mid))
            }
        }
        totalTime += Double(dist[dist.count - 1])/Double(mid)
        // print(totalTime)
        if totalTime <= hour {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return left
}


// let dist = [1,3,2]
// let hour: Double = 6

// let dist = [1,3,2]
// let hour: Double  = 2.7

// let dist = [1,1,100000]
// let hour: Double  = 2.01

// let dist = [47,40,31,8,31,73,11,11,94,63,9,98,69,99,17,17,85,61,71,22,34,68,78,55,28,70,97,94,89,26,92,40,52,86,84,48,57,67,58,16,32,29,9,44,3,76,71,30,76,29,1,10,91,81,8,30,9]
// let hour: Double  = 73.58

// let dist = [10]
// let hour: Double  = 5.52

let dist = [3,3]
let hour: Double  = 2.0

/// 

/// how do you choose yoru boudns for left and right? 
print(dist.count)
let sum = dist.reduce(0, +)
// print(sum)
print(minSpeedOnTime(dist, hour))