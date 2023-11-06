class Solution {
    func countLargestGroup(_ n: Int) -> Int {

        var digitSum = [Int: [Int]]()
        for i in 1...n {
            let char = Array(String(i))
            var charSum = 0
            for c in char {
                if let num = Int(String(c)) {
                    charSum += num
                } 
            }
            if digitSum[charSum] == nil {
                digitSum[charSum] = [i]
            } 
            else {
                digitSum[charSum]!.append(i)
            }
        }
        var maxLength = 0
        for (_, value) in digitSum{
            maxLength = max(maxLength, value.count)
        } 

        var res = 0
        for (_, value) in digitSum{
            if maxLength == value.count {
                res += 1
            }
        } 
        return res
    }
}



let s = Solution()
print(s.countLargestGroup(13))