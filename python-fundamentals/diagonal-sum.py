def diagonalSum(mat):
    sumList = []
    dim_matrix = len(mat)
    for i in range(0,dim_matrix):
        j = dim_matrix - i - 1
        if i !=j:
            sumList.append(mat[i][i])
            sumList.append(mat[i][j])
        else:
            sumList.append(mat[i][j])
    print(sumList)
    return sum(sumList)


mat = [[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]

diagonalSum(mat)