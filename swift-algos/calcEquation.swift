

// build adjacency dictionary 


// then do bfs on the query until you arrive at the destination
// use bfs to minimize the traversal 



func calcEquation(_ equations: [[String]], _ values: [Double], _ queries: [[String]]) -> [Double] {


    // build adjacency dictionary 
    var graph = [String: [(String, Double)]]()

    for (i, coords) in equations.enumerated() {
        let u: String = coords[0]
        let v: String = coords[1]
        let val = values[i]
        if let _ = graph[u] {
            graph[u]!.append((v, val))
        } else {
            graph[u] = [(v, val)]
        }

        if let _ = graph[v] {
            graph[v]!.append((u, 1/val))
        } else {
            graph[v] = [(u, 1/val)]
        }
    }
    print(graph)


    // define bfs

    func bfs(_ u: String, _ v: String) -> Double {
        var queue: [String] = []
        var start: String = u





        return 1.0
    }


    // now for each query, bfs

    return [1, 2]
}


var equations = [["a","b"],["b","c"]]
var values = [2.0,3.0]
var queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

var x = calcEquation(equations, values, queries)


var queue = Deque<String>  