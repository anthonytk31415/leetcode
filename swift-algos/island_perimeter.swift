print("Hello World")

// scan through the grid for the first land; stop after
// then dfs the first land, and then count the perimeter for that cell and then call dfs on each of the adjacent 
// cells that have not been visited

let arr = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

func findPerimeter(arr: [[Int]]) -> Int {

    func findFirst(arr:[[Int]]) -> (Int, Int) {
        for (i, row) in arr.enumerated(){
            for (j, _) in row.enumerated(){
                let entry = arr[i][j]
                print(entry)
                if entry == 1 {
                    return (i, j)
                }
            }
        }
        return (-1, -1)
    }

    var visited: [[Int]] = []
    for (_, row) in arr.enumerated() {
        var cur_row: [Int] = []
        for (_ , _) in row.enumerated() {
            cur_row.append(0)
        }
        visited.append(cur_row)
    }

    let rowMax = arr.count
    let colMax = arr[0].count 

    func dfs(i: Int, j:Int) {
        // find the perimeter
        for (x, y) in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]{
            if y < 0 || y >= colMax || x < 0 || x >= rowMax || arr[x][y] == 0 {
                perimeter += 1
            }
        }
        // call dfs recursively
        for (x, y) in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]{
            if x >= 0 && x < rowMax && y >= 0 && y < colMax && visited[x][y] == 0 && arr[x][y]==1{
                visited[x][y] = 1
                dfs(i:x, j:y)
            }
        }    
    }

    var perimeter = 0
    let firstIdx = findFirst(arr: arr)
    let (x,y) = firstIdx
    visited[x][y] = 1
    dfs(i: x, j: y)
    return perimeter
}

print(findPerimeter(arr: arr))