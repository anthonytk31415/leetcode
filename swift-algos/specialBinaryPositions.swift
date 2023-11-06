class Solution {
    func numSpecial(_ mat: [[Int]]) -> Int {
        var count = 0
        for i in 0..<mat.count{
            let rowSum = mat[i].reduce(0, +)
            if rowSum == 1 {
                for j in 0..<mat[0].count{
                    if mat[i][j] == 1 {
                        var all_zero = true 
                        for k in 0..<mat.count{
                            if i != k && mat[k][j] != 0{
                            all_zero = false
                            break
                            }
                        }
                        if all_zero == true {
                            count += 1
                        }
                        break
                    }
                }
            }
        }
        return count
    }
}

// let mat = [[1,0,0],[0,0,1],[1,0,0]]
let mat = [[1,0,0],[0,1,0],[0,0,1]]
let sol = Solution()
print(sol.numSpecial(mat))
