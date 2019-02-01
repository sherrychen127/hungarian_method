

def hungarianMethod(matrix):
    deleted_col = []
    deleted_row = []
    marked = []

    #step1: row reductioin and col reduction
    matrix = row_reduction(matrix)
    matrix = col_reduction(matrix)

        #step2: row scanning (&col scanning)
        #row scanning: if the row has exactly one zero, mark the zero and draw a vertical line
    matrix = cover_zero(matrix, deleted_row, deleted_col)
    marked = find_assignment(matrix, marked)


    return marked

def row_reduction(matrix):
    for row in matrix:
        min = find_min(row)
        if min is not None:
            for i in range(len(row)):
                row[i] = row[i] - min
    print("done row redution")
    print(matrix)
    return matrix

def col_reduction(matrix):

    for j in range(len(matrix)):
        min = 10000
        for i in range(len(matrix)):
            if matrix[i][j] < min:
                min = matrix[i][j]

        if min < 10000:
            for i in range(len(matrix)):
                matrix[i][j]-=min
    print("done col reduction")
    print(matrix)
    return matrix



def cover_zero(matrix, deleted_row, deleted_col):
    count = 0
    done = 0
    while not done:
        #initialize
        count = 0

        for i in range(len(matrix)):
            N = len(matrix) - i

            for row in range(len(matrix)):
                if row not in deleted_row and zero_count(matrix[row], deleted_col) == N:
                    count += 1
                    deleted_row.append(row)

            for col in range(len(matrix)):
                col_arr = []
                if col not in deleted_col:
                    for row in range(len(matrix)):

                        col_arr.append(matrix[row][col])
                if zero_count(col_arr, deleted_row) == N and col not in deleted_col:
                    count += 1
                    deleted_col.append(col)

        if count == len(matrix):
            done = 1
        else:
            matrix = adjust_matrix(matrix, deleted_row, deleted_col)
            deleted_col = []
            deleted_row = []

    return matrix




def find_assignment(matrix, marked):
    deleted_row = []
    deleted_col = []
    count = 0
    while True:
        count += 101
        if count > 100:
            return compromised(matrix,marked, deleted_col, deleted_row)
        for i in range(1, len(matrix)+1):
            for row in range(len(matrix)):
                if zero_count(matrix[row], []) == i:
                    for col in range(len(matrix)):
                        if matrix[row][col] == 0 and row not in deleted_row and col not in deleted_col:
                            deleted_col.append(col)
                            deleted_row.append(row)
                            tuple = (row, col)
                            marked.append(tuple)
                            break

            for col in range(len(matrix)):
                col_arr = []
                for row in range(len(matrix)):
                    col_arr.append(matrix[row][col])
                if zero_count(col_arr, deleted_row) == i:
                    for row in range(len(matrix)):
                        if matrix[row][col] == 0 and row not in deleted_row and col not in deleted_col :
                            deleted_row.append(row)
                            deleted_col.append(col)
                            tuple = (row,col)
                            marked.append(tuple)
        #print("marked len:",len(marked))
        #print("matrix len:", len(matrix))
        if len(marked) == len(matrix):
            break
        else:
            matrix = adjust_matrix(matrix, deleted_row,deleted_col )
            marked = []
            deleted_row = []
            deleted_col = []
    return marked


def adjust_matrix(matrix, deleted_row, deleted_col):
    remain_arr = []
    min = 100000
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i not in deleted_row and j not in deleted_col:
                if matrix[i][j] < min:
                    min = matrix[i][j]
                tuple = (i,j)
                remain_arr.append(tuple)
    if min == 100000:
        return matrix
    for index in remain_arr:
        matrix[index[0]][index[1]] -= min
    print("done adjusting matrix", matrix)
    return matrix


def compromised(matrix, marked, deleted_col, deleted_row):
    full = []
    for i in range(len(matrix)):
        full.append(i)
    for i in full:
        if i not in deleted_row:
            ind = -1
            min = 1000
            for j in range(len(matrix[i])):
                if j not in deleted_col and matrix[i][j] < min:
                    min = matrix[i][j]
                    ind = j

            marked.append((i,ind))
            deleted_row.append(i)
            deleted_col.append(ind)
    return marked


def find_min(arr):
    #@INPUT: 1D array
    #@RETURN: minimum value
    if len(arr) == 0:
        return None
    min = arr[0]
    for entry in arr:
        if entry<min:
            min = entry

    return min


def zero_count(arr, deleted_arr):
    #@input(array, array)
    #@RETURN: integer (count of 0)
    count = 0
    for i in range(len(arr)):
        if i not in deleted_arr and arr[i] == 0:
            count += 1
    return count



if __name__ == '__main__':
    matrix = [[0, 4, 2, 4, 0, 2], [2, 4, 6, 0, 4, 2], [6, 0, 2, 4, 4, 2], [4, 2, 6, 2, 4, 0], [2, 2, 6, 0, 4, 0], [2, 2, 0, 6, 0, 4]]
    marked = hungarianMethod(matrix)
    print(marked)

