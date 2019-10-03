def solve(matrix, n, m, cur_row):
    print(matrix, cur_row)
    if cur_row == n:
        print('basecase')
        return [[]]

    zeros = []
    for i in range(len(matrix[cur_row])):
        if matrix[cur_row][i] == 0:
            zeros.append((cur_row, i))


        # total_assigned.append(assigned)
    assigned = []
    # total_assigned = []
    if zeros == []:
        assigned = solve(matrix, n, m, cur_row + 1)
    for zero in zeros:
        prev_assigned = solve(matrix, n, m, cur_row + 1)
        for assign in prev_assigned:
            if check_valid(assign, zero):
                print('valid')
                assign.append(zero)
            assigned.append(assign)
                # total_assigned.append(assigned)
                # print(total_assigned)
    # print(cur_row)
    # print('total_assigned', total_assigned)

    # max_assigned = total_assigned[0]
    # for assign in total_assigned:
    #     if len(assign) > len(max_assigned):
    #         max_assigned = assign

    # print('gonna return,', max_assigned)
    return assigned


def check_valid(assigned, zero):
    for assign in assigned:
        if zero[0] == assign[0] or zero[1] == assign[1]:
            return False
    return True


if __name__ == '__main__':
    matrix = [[0, 8, 0, 0], [0, 15, 17, 20], [19, 0, 0, 3], [0, 9, 8, 0]]
    n = 4
    m = 4
    assigned = solve(matrix, n, m, 0)
    max_assign = assigned[0]
    for assign in assigned:
        if len(assign) > len(max_assign):
            max_assign = assign
    print(max_assign)
