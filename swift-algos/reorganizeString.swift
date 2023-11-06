


func reorganizeString(_ s: String) -> String {
    
    var countLetters: [String.Element: Int] = [:]
    // var maxChar: String.Element? = nil
    var maxCharCount = 0

    for (_, char) in s.enumerated() {
        if let _ = countLetters[char]{
            countLetters[char]! += 1
        } else {
            countLetters[char] = 1
        }
        if countLetters[char]! > maxCharCount {
            maxCharCount = countLetters[char]!
            // maxChar = char
        }
    }
    let z: Double = Double(s.count)/2 
    if Double(maxCharCount) > z.rounded() {
        return ""
    }

    var maxHeap: [(Int, String.Element)] = []
    for (char, num) in countLetters {
        maxHeap.append((num, char))
    }
    maxHeap.sort{$0.0 < $1.0}
    var countChar = [Int]()
    var letterOrder = [String]()

    for (num, char) in maxHeap {
        countChar.append(num)
        letterOrder.append(String(char))
    }

    var res = ""
    var idx = countChar.count - 1
    var i = 0
    while i < s.count {
        if countChar[idx] > 0 {
            res += letterOrder[idx]
            countChar[idx] -= 1
            i += 1
        }
        idx -= 1
        if idx < 0 {
            idx = countChar.count - 1
        }
    }
    return res  
}

print(reorganizeString("abracadabra"))


// aabababaaacccccc
// let x = "anthony"
// for (_, char) in x.enumerated() {
//     print(char)
// }


// // for even length strings: 
// // if the count of any char is longer than half: return ""

// // for odd length strings: 
// // if the count of any char is longer than half rounded up: return ""



// print(Double(55/2).rounded())

// you always want to put the largest count element first, 
// this is an nlogn algo potentially