func findContentChildren(_ g: [Int], _ s: [Int]) -> Int {
    
    var gs = g.sorted(by: <)
    var ss = s.sorted(by: <)
    var g_idx = 0
    var s_idx: Int = 0

    while g_idx < g.count && s_idx < s.count {
        print(g_idx, s_idx, g[g_idx], s[s_idx])
        if gs[g_idx] <= ss[s_idx] {
            g_idx += 1
        }
        s_idx += 1
    }
    return g_idx     
}

// var g = [1,2,3]
// var s = [1,1]

//  g = [1,2], s = [1,2,3]

var g: [Int] = [1,2] 
var s: [Int] = [1,2,3]

print(findContentChildren(g, s))


// var arr = [(1,2), (-1,3), (7, -2)]

// arr.sort(by: {$0.0 < $1.0})
// print(arr)