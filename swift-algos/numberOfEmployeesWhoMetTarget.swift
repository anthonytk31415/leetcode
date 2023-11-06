func numberOfEmployeesWhoMetTarget(_ hours: [Int], _ target: Int) -> Int {
    var res: Int = 0
    for num in hours {
        if num >= target {
            res += 1 
        }
    }
    return res
}