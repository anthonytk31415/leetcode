func findComplement(_ num: Int) -> Int {
    let binaryRep = String(num, radix:2)
    var complement = ""
    for char in binaryRep{
        if char == "0" {
            complement += "1"
        } else if char == "0" {
            complement += "1"
        }
    }

    return Int(complement, radix: 2) ?? 0
}


print(findComplement(1002))