from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def vertex_to_edges(edges, vertex):
            return list(filter(lambda x: x[1] == vertex, edges))

        def vertex_from_edges(edges, vertex):
            return list(filter(lambda x: x[0] == vertex, edges))
        
        all_nodes = set([x for x in range(n)])
        nodes_with_path_to = set([x[1] for x in edges])         ## get list of vertices with path to (i.e. [1,2] means 2 has a "path to")

        