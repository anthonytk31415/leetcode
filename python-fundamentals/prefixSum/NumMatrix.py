class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[x for x in matrix[i]] for i in range(len(matrix))]
        print(self.prefix)
        self.constructPrefix()

    def constructPrefix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if i == 0 and j == 0: 
                    self.prefix[i][j] = self.prefix[i][j]  
                elif i == 0: 
                    self.prefix[i][j] = self.prefix[i][j-1] + self.prefix[i][j]
                elif j == 0:
                    self.prefix[i][j] = self.prefix[i-1][j] + self.prefix[i][j] 
                else: 
                    self.prefix[i][j] = self.prefix[i][j-1] + self.prefix[i][j] + self.prefix[i-1][j] - self.prefix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.prefix[row2][col2]
        if row1 - 1 >= 0: res -= self.prefix[row1 -1][col2]           
        if col1 - 1 >=0: res -= self.prefix[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0: res += self.prefix[row1 - 1][col1 - 1]
        return res

mat = NumMatrix(matrix)
print(mat.prefix)