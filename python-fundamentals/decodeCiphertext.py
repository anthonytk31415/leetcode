def decodeCiphertext(encodedText, rows):
    cols = int(len(encodedText)/rows)
    ## convert to matrix
    matrix = []
    cur_row = []
    for x in encodedText: 
        cur_row.append(x)
        if len(cur_row) == cols: 
            matrix.append(cur_row)
            cur_row = []

    res = ''
    ## iterate for each diagonal
    for j in range(len(matrix[0])):
        i = 0
        while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            res = res + matrix[i][j]
            i +=1
            j +=1

    idx = len(res)
    for i in range(len(res)-1, -1, -1): 
        if res[i] == ' ':
            idx -=1
        else: 
            break
    return res[:idx]

# encodedText = "ch   ie   pr"
# rows = 3

encodedText = "coding"
rows = 1
print(decodeCiphertext(encodedText, rows))