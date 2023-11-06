from collections import deque

# Time: O(n)
# Space: O(n) in matrix form


def convert(s, numRows):
    if numRows == 1: 
        return s
    
    s = deque([x for x in s])
    matrix = []
    reg = True
    while s: 
        cur_row = deque()
        if reg == True:
            for _ in range(numRows):
                if s: 
                    cur_row.append(s.popleft())
                else: 
                    cur_row.append("#")
        if reg == False: 
            cur_row.appendleft('#')
            for _ in range(numRows - 2):
                if s: cur_row.appendleft(s.popleft())
                else: cur_row.appendleft('#')
            cur_row.appendleft('#')
        matrix.append(cur_row)
        reg = not reg
    
    # print(matrix)
    res = []
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] != '#':
                res.append(matrix[i][j])
    return ''.join(res)

s = "ABCDE"
numRows = 4
print(convert(s, numRows))

        