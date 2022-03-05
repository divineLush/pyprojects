ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def transpose(matrix):
    res = []
    ln = len(matrix[0])

    for pos in range(ln):
        transp_row = [row[pos] for row in matrix]
        res.append(transp_row)


    return res


print(transpose(ex))
