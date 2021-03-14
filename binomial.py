def row_array(rows, columns, default_val):
	return [ [default_val for j in range (0,columns)] for i in range(0,rows)] #[[default_val] * columns] * rows

def generate_lookup(size):
	A = row_array(size,size,0)

	for i in range(0,size):
		A[i][0]=1
		A[i][i]=1

	for k in range(1,size):
		for j in range(k+1,size):
			A[j][k] = A[j-1][k-1] + A[j-1][k]
	
	return A	