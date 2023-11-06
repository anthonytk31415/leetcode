// if youre at the end, increment by 1
// start at the top: 0,0
// dfs right and down if there are no obstacles or walls
//  
func uniquePathsWithObstacles(_ obstacleGrid: [[Int]]) -> Int {

    var paths: [[Int?]] = obstacleGrid.map({row in row.map({ x in nil})})

    let m = obstacleGrid.count - 1
    let n = obstacleGrid[0].count - 1

    // if paths is nil then go through the iteration
    // if its the end, the counter += 1 and map
    // if it's not then dfs for each cell and add it to the counter
    // then at the end paths(i,j) = counter 
    // return the paths(i,j)

    func dfs(_ i: Int, _ j: Int) -> Int {
        // print(i, j)
        var counter: Int = 0

        if paths[i][j] == nil {
            if i == m && j == n {
                counter += 1
            } else {
                for (u, v) in [(i + 1, j), (i, j + 1)] {
                    if u <= m && v <= n && obstacleGrid[u][v] == 0 {
                        counter += dfs(u,v)
                    } 
                }
            }
            paths[i][j] = counter
        }
        return paths[i][j] ?? 0
    }

    var res: Int = 0
    if obstacleGrid[0][0] == 0 {
        res = dfs(0,0)
    }
    return res
}
// [[0,0,0,0],[0,1,0,0],[0,0,0,0]]
// var obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
var obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0]]

// var x: [Int] = [3,5]
// var y: [Int] = x.map( {(num: Int) -> Int in return(num*2)})
// print(x, y)

// var res: [[Int]] = obstacleGrid.map({(arr: [Int]) -> [Int] in return (arr.map({(num: Int) -> Int in return (0)}))})

// var res2 = obstacleGrid.map({row in row.map({ x in 0})})

// print(res2)
print(uniquePathsWithObstacles(obstacleGrid))