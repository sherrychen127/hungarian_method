
import pprint
def hungarian_method(matrix):
	#STEP1
	#row_deduction
	(n,m)=(len(matrix), len(matrix[0]))
	new_matrix=[]
	for row in matrix:
		row_min=min(row)
		new_matrix.append([x-row_min for x in row])
	pprint.pprint('after step 1:')
	pprint.pprint(new_matrix)
	
	#get row
	#STEP3:
	count=0
	while(1):
		count+=1
		assigned = solve(new_matrix, n, m, 0)
		# print('assigned:{}'.format(assigned))

		max_assign = assigned[0]
		for assign in assigned:
			if len(assign) > len(max_assign):
				max_assign = assign

		print('max_assign',max_assign)

		if len(max_assign) == min(n,m):
			print(max_assign)
			return 

		# if count==5:
		# 	return

				


		mark_matrix=new_matrix
		pprint.pprint(mark_matrix)
		
		marked_rows=[]
		marked_cols=[]

		assigned_rows = [x[0] for x in max_assign]
		print(assigned_rows)
		#1. tick all unassigned rows
		#2. tick all (unticked) columns that have zeros in ticked rows
		#3. tick all unticked rows that have assigned zeros in ticked columns

		for i in range(n):
			if i not in assigned_rows:
				rows=[i]
				row=True
				done=False
				while(1):
					print('it')
					if row:
						done=True
						for r in rows:
							if r in marked_rows:
								continue
							print('add rows:{}'.format(rows))
							marked_rows.append(r)
							cols = []
							for j in range(m):
								if mark_matrix[r][j] == 0 and j not in marked_cols:
									print('found new cols:{}'.format(j))
									row=False
									cols.append(j)
									done=False
							continue
						if done:
							# marked_cols.append(cols)
							break
		
					else:
						done=True
						for c in cols:
							if c in marked_cols:
								continue
							print('add cols:{}'.format(cols))
							marked_cols.append(c)
					
							rows = []
							for j in range(n):
								print(j,c)
								if mark_matrix[j][c] == 0 and j not in marked_rows and (j,c) in max_assign:
									print('found new rows:{}'.format(j))
									row=True
									rows.append(j)
									done=False
						if done:
							# marked_rows.append(rows)
							break
					
					

		print('marked_rows')
		print(marked_rows, marked_cols)
		print(mark_matrix)
		

		draw_cols = marked_cols
		draw_rows = [x for x in range(n) if x not in marked_rows]
		print('drawed:{}, {}'.format(draw_rows, draw_cols))

		not_drawed_cols = [x for x in range(m) if x not in draw_cols]
		not_drawed_rows = [x for x in range(n) if x not in draw_rows]
		print('not_drawed:{},{}'.format(not_drawed_rows, not_drawed_cols))
		unmarked = [mark_matrix[i][j] for i in not_drawed_rows for j in not_drawed_cols]
		print('unmarked:{}'.format(unmarked))

		unmarked_min = min(unmarked)
		for i in range(n):
			for j in range(m):
				if i in draw_rows and j in draw_cols:
					mark_matrix[i][j] += unmarked_min
				elif i in not_drawed_rows and j in not_drawed_cols:
					mark_matrix[i][j] -= unmarked_min

		
		pprint.pprint(mark_matrix)
		new_matrix=mark_matrix







		

def solve(matrix, n, m, cur_row):
    print(matrix, cur_row)
    if cur_row == n:
        print('basecase')
        return [[]]

    zeros = []
    for i in range(len(matrix[cur_row])):
        if matrix[cur_row][i] == 0:
            zeros.append((cur_row, i))

    assigned = []
    if zeros == []:
        assigned = solve(matrix, n, m, cur_row + 1)
    for zero in zeros:
        prev_assigned = solve(matrix, n, m, cur_row + 1)
        for assign in prev_assigned:
            if check_valid(assign, zero):
                print('valid')
                assign.append(zero)
            assigned.append(assign)
    return assigned


def check_valid(assigned, zero):
    for assign in assigned:
        if zero[0] == assign[0] or zero[1] == assign[1]:
            return False
    return True



def main():
	test_case_1=[[0,1,2,3],
				[1,0,3,0],
				[0,2,1,3],
				[1,0,1,3]]

	test_case_2=[[0,1,2,3],
				[1,2,3,0],
				[0,2,1,3]]

	test_case_3 = [
				 [20,28,19,13],
				 [15,30,31,28],
				 [40,21,20,17],
				 [21,28,26,12]]
	test_matrix=test_case_3
	hungarian_method(test_matrix)

if __name__ == '__main__':
	main()