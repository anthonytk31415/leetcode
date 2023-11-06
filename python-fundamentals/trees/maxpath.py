# max path\\\


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

def rootToGraph(root):
    graph = Graph()
    def helper(root, graph, parent=None):
        if root: 
            graph.g[root]
            if parent: 
                graph.g[root].append(parent)
            for child in [root.left, root.right]:
                if child: 
                    graph.g[root].append(child)
                    helper(child, graph, root)
    helper(root, graph)
    return graph

# start = root.val

def dfs(graph,start):
    status = {}
    maxPathAndNode = {'node':start, 'max': start.val}

    for v in graph.g:
        status[v] = {'visited': False, 'processed': False, 'maxPath': None, 'parent':None}

    def dfs_helper(start, status, maxPathAndNode):
        status[start]['visited'] = True
        curParent = status[start]['parent']
        if curParent != None:
            status[start]['maxPath'] = max(start.val, status[curParent]['maxPath'] + start.val) 
        elif status[start]['maxPath'] == None and curParent == None:
            status[start]['maxPath'] = start.val
        for v in graph.g[start]:
            if status[v]['visited'] == False:
                status[v]['parent'] = start
                dfs_helper(v, status, maxPathAndNode)
        status[start]['processed'] = True    
        if status[start]['maxPath'] > maxPathAndNode['max']:
            maxPathAndNode['max'] = status[start]['maxPath']
            maxPathAndNode['node'] = start

    dfs_helper(start, status, maxPathAndNode)
    return maxPathAndNode


def maxPathSum(root):
    graph = rootToGraph(root)
    node1 = root
    path1 = dfs(graph, node1)
    node2 = path1['node']
    path2 = dfs(graph, node2)
    return path2['max']



# root = TreeNode(0)
# root.left = TreeNode(1)
# root.right = TreeNode(1)


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# root = TreeNode(-20)
# root.left = TreeNode(5)
# root.right = TreeNode(25)
# root.right.right = TreeNode(-30)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(-10)

# graph = rootToGraph(root)
# print(graph.g)


# x = dfs(graph, root)
# print(x)

# y = maxPathSum(root)
# print(y)

# j = 0 = i - 1
# i = 1 --> j = 0
# i - 1 = j
# i = j + 1

# for i = 1: start --> j = 0
# i = j-1 --> j = 0
# left(i) = (2i) = 2(j+1)
# right(i) = (2i+1) = 2(j-1) + 1
# parent(i) = i//2 = (j-1)//2

def arrayToTree(a):
    # start from i = 1 = j - 1; i.e. j = 0
    def helper(a, j):
        if j < len(a) and a[j] != None:
            newNode = TreeNode(a[j])
            newNode.left = helper(a, 2*j)
            newNode.right = helper(a, 2*(j) + 1)
            return newNode
        else: 
            return None
    return helper(a, 1)

# z = [0]+[-633,-237,447,-740,149,-264,-314,-484,-938,706,-483,-542,575,132,101,-220,-805,-43,None,371,318,-294,-611,-236,152,-171,398,598,531,None,-181,11,None,-643,577,735,-409,163,178,-879,-929,936,-658,826,461,-55,-579,None,None,None,None,-384,974,426,-899,-476,83,-900,-929,661,None,11,986,None,None,-194,-840,991,75,-662,None,-3,None,None,None,-906,None,716,-479,-895,902,None,None,-507,None,-695,None,None,None,424,33,None,-556,-312,None,-916,None,617,None,-623,110,None,None,None,None,-309,118,None,None,-128,-899,12,561,-163,869,-501,-811,308,979,None,846,-860,7,None,None,-782,None,None,-754,100,None,None,None,None,None,None,None,707,504,800,-59,None,None,None,None,302,None,399,None,None,None,None,None,None,None,-328,None,289,-81,None,-241,-266,None,None,507,-363,None,94,None,-891,None,969,-339,146,None,-520,None,None,None,None,None,None,None,-718,None,206,None,None,None,None,None,-509,-678,None,None,None,-838,None,None,None,None,-398,None,-630,618,-879,620,None,-606,-387,-275,None,129,490,-312,813,650,-296,-970,481,-271,None,-118,None,-822,None,None,None,None,None,None,-369,-453,None,None,490,None,None,-517,131,-264,None,None,None,None,551,978,None,None,532,-181,531,None,638,None,-447,-705,4,-506,None,278,None,None,None,56,None,None,425,237,None,462,39,None,546,766,-164,-102,None,None,-497,267,None,None,-238,483,None,None,773,388,-195,305,None,None,None,None,None,None,None,None,None,None,-742,None,-507,None,None,None,None,None,None,None,None,None,None,None,None,None,197,None,None,-72,None,None,None,None,None,None,None,-933,None,-749,-594,None,None,None,-569,127,-321,None,-391,None,230,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-341,-527,None,None,122,146,None,None,None,-236,-332,None,None,-812,None,None,114,None,None,-549,None,152,146,None,-842,None,448,977,None,None,None,97]


z = [0] + [-10, 9, 20, None, None, 15, 7]
root_z = arrayToTree(z)

print(root_z)
print(len(z))

y = maxPathSum(root_z)
print(y)
print(maxPathSum(root))