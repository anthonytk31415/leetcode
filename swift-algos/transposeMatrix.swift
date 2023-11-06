class Solution1 {
    func transpose(_ matrix: [[Int]]) -> [[Int]] {
        var res = [[Int]]()
        for _ in 0..<matrix.count {
            res.append([Int]())
        }

        for row in 0..<matrix.count{
            for col in 0..<matrix[0].count{
                res[col].append(matrix[row][col])
            }
        }
        return res
    }
}

class Solution {
    func transpose(_ matrix: [[Int]]) -> [[Int]] {
        var res = Array(repeating: Array(repeating: 0, count: matrix.count), count: matrix[0].count)

        for row in 0..<matrix.count{
            for col in 0..<matrix[0].count{
                res[col][row] = matrix[row][col]
            }
        }
        return res
    }
}


let matrix = [[1,2,3],[4,5,6],[7,8,9]]
let solution = Solution()
print(solution.transpose(matrix))
