class Solution {
    func diagonalSum(_ mat: [[Int]]) -> Int {
        var res = 0
        for i in 0..<mat.count{
            res += mat[i][i]
        }
        for i in 0..<mat.count{
            if mat.count - 1 - i != i {
                res += mat[mat.count - 1 - i][i]
            }
            
        }
        return res
    }
}

let mat = [[1,2,3],
           [4,5,6],    
           [7,8,9]]

let s = Solution()
print(s.diagonalSum(mat))