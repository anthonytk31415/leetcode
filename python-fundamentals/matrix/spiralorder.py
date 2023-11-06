# spiralorder


def spiralorder(matrix):
    def removetop(matrix):
        return matrix[1:]
    def removeright(matrix):
        if matrix[0][:-1] == []:
            return []
        else:
            return [x[:-1] for x in matrix]
    def removebot(matrix):
        return matrix[:-1]
    def removeleft(matrix):
        if matrix[0][1:] == []:
            return []
        return [x[1:] for x in matrix]
    
    
    def helper(matrix, lastOp, res):
        lastOp = (lastOp + 1) % 4
        # print(matrix)
        if matrix:
            if lastOp == 0:
                res = res + matrix[0]
                return helper(removetop(matrix), lastOp, res)
            elif lastOp == 1:
                res = res + [x[-1] for x in matrix]
                return helper(removeright(matrix), lastOp, res)          
            elif lastOp == 2:
                res = res + list(reversed(matrix[-1]))
                return helper(removebot(matrix), lastOp, res)
            elif lastOp == 3:
                tmp = [x[0] for x in matrix]
                res = res + list(reversed(tmp))
                return helper(removeleft(matrix), lastOp, res)
        else: 
            return res
    return helper(matrix, 3, [])


# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(spiralorder(matrix))


matrix = [[7],[9],[6]]

print(spiralorder(matrix))

# another trick: 
# increment by direction dx, dy starting with (1,0) = (dx, dy); 
# when you get out of bounds or hit a visited entry (denoted by "*"), do 
# dx, dy = -dy, dx to reverse the direction of which entry you traverse


def spiralOrder2(matrix):
    n, m = len(matrix[0]), len(matrix)
    x, y, dx, dy = 0, 0, 1, 0
    ans = []
    for _ in range(m*n):
        if not 0 <= x+dx < n or not 0 <= y+dy < m or matrix[y+dy][x+dx] == "*":
            dx, dy = -dy, dx
            
        ans.append(matrix[y][x])
        matrix[y][x] = "*"
        x, y = x + dx, y + dy
    
    return ans