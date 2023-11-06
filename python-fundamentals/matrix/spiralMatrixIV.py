# spiral matrix iv

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# spiralMatrix

def spiralMatrix(m, n, head):
    grid = [[-1 for _ in range(n)] for _ in range(m)]
    cur_dir = 'r'
    change_dir = {'r':'d' , 'd':'l', 'l':'u','u':'r'}
    l_bound = 0
    r_bound = n-1
    u_bound = 0
    d_bound = m-1
    node = head
    i, j = 0, 0
    dir_increment = {'r': [0,1] , 'd': [1,0], 'l':[0,-1],'u':[-1,0]}
    decrease_bounds = {'r': [0,0,1,0] , 'd': [0,-1,0,0], 'l':[0,0,0,-1],'u':[1,0,0,0]}      # l, r, u, d
    x, y = dir_increment[cur_dir]
    while node != None: 
        # you'll always be in an empty spot and in a valid spot
        print(i, j)
        if grid[i][j] == -1: 
            # print(node, node.val)
            grid[i][j] = node.val
            node = node.next            

        # if youre at the end (the next step will kick you off bounds) -> change dir and then increment
        # otherwise, just increment
        if not (u_bound <= i + x <= d_bound and l_bound <= j + y <= r_bound):
            # update bounds
            l_plus, r_plus, u_plus, d_plus = decrease_bounds[cur_dir]
            l_bound, r_bound, u_bound, d_bound =  l_bound + l_plus, r_bound + r_plus, u_bound + u_plus, d_bound + d_plus

            # update direction and increment 
            cur_dir = change_dir[cur_dir]
            x, y = dir_increment[cur_dir]

        # update the index
        i +=x
        j +=y

    return grid

m = 3
n = 5 
head = [3,0,2,6,8,1,7,9,4,2,5,5,0]

root = ListNode(head[0])
node = root
for x in head[1:]:
    node.next = ListNode(x)
    node = node.next

print(root)
node = root
while node: 
    print(node.val)
    node = node.next

print(spiralMatrix(m, n, root))