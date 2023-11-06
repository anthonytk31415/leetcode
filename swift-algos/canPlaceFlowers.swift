func canPlaceFlowers(_ flowerbed: [Int], _ n: Int) -> Bool {
    var zeroes: Int = 1
    var newFlowers: Int = 0
    for (i, val) in flowerbed.enumerated() {

        if val == 1 {
            zeroes = 0
        } else if val == 0 {
            zeroes += 1
            if i == flowerbed.count - 1 {
                zeroes += 1
            }
            if zeroes >= 3 {
                newFlowers += 1
                zeroes = 1
            }
        }

        print(zeroes, newFlowers)
        if newFlowers >= n {
            return true 
        }

    }
    return false 
}

// let flowerbed = [1,0,0,0,1]
// let n = 1

let flowerbed = [1,0,0,0]
let n = 1

// let flowerbed = [1,0,0,0,1]
// let n = 2

print(canPlaceFlowers(flowerbed, n))