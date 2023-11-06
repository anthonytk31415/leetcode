// func arrangeCoins(_ n: Int) -> Int {  
//     var res: Int = 0
//     var remaining: Int = n
//     var curRow: Int = 1

//     while true {
//         if remaining - curRow >= 0 {
//             res += 1
//             remaining -= curRow
//             curRow += 1 
//         } else {
//             break 
//         }
//     }
//     return res
// }

// you solve this using binary search
// sum = n*(n+1)/2 where n is the sum of first n natural numbers


// while left < right: 
// start with left = 1, right = n
// take the midpoint; 

// if sum(midpoint) < n:
//  left = midpoint; 
// if sum(midpoint) == n: return midpoint 
// if sum(midpoint) > n:
//  right = midpoint 
// when you exit the while loop: 
// return right


func arrangeCoins(_ n: Int) -> Int {  
    var left = 1
    var right = n
    while left < right{
        // print(left, right)
        let midpoint: Int = (left + right)/2
        let curSum = midpoint*(midpoint + 1)/2
        if curSum < n {
            left = midpoint + 1
        } else if curSum > n {
            right = midpoint - 1
        } else {
            return midpoint
        }
    }
    return right
}

print(arrangeCoins(5))