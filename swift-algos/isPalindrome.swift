// 

func isPalindrome(_ x: Int) -> Bool {
    if x < 0 {
        return false
    } else if x == 0 {
        return true
    }

    var arr: [Character] = []
    for char: Character in String(x){
        arr.append(char)
    }
    var i = 0
    var j: Int = arr.count - 1
    while i < j {
        if arr[i] != arr[j] {
            return false
        }
        i += 1
        j -= 1
    }
    return true

}

// let a = 123 
// let b: String = String(a)
// print(b)

print(isPalindrome(1112111))