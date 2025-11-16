def saddle_points(matrix):
    for index in range(1, len(matrix)):
        if len(matrix[index-1]) != len(matrix[index]):
            raise ValueError("irregular matrix")
    row=[]
    column=[]
    result=[]
    for item in matrix:
        row.append(max(item))
    transpose=list(zip(*matrix))
    for item in transpose:
        column.append(min(item))
    for index_column, item_column in enumerate(column):
        for index_row, item_row in enumerate(row):
            if item_row == item_column:
                result.append({'column':index_column+1, 'row':index_row+1})
    return result