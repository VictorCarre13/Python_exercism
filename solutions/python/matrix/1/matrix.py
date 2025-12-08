class Matrix:
    def __init__(self, matrix_string):
        row=[]
        save=[]
        number=""
        for index in range(0,len(matrix_string)):
            if matrix_string[index]=='\n':
                row.append(save)
                save=[]
            if index < len(matrix_string)-1:
                if matrix_string[index].isdigit() and not matrix_string[index+1].isdigit():
                    number+= matrix_string[index]
                    save.append(int(number))
                    number=""
                else:
                    number+= matrix_string[index]
            elif matrix_string[index].isdigit():
                number+= matrix_string[index]
                save.append(int(number))
                number=""
        row.append(save)
        self.rows=row
        self.columns=list(zip(*row))
        
    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return list(self.columns[index-1])
