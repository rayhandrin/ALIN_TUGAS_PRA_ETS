def print_m(matrix):
	# This function will print all of the matrix elements

	for i in matrix:
		print(i)

def init_m():
	# This function will initialize and return a matrix
	# with desired row and column length
	matrix = []

	print('Panjang baris: ', end = '')
	row_len = int(input())
	print('Panjang kolom: ', end = '')
	col_len = int(input())

	for i in range(row_len):
		matrix.append([])
		for j in range(col_len):
			matrix[i].append(0)
			print('Masukkan nilai untuk baris ke-{} kolom ke-{}: '.format(i+1, j+1), end='')
			matrix[i][j] = int(input())

	return matrix

def m_multiply(f_matrix, s_matrix):
	# This function will multiplies two matrices.
	# and will return the result matix if the arguments pass the checking process
	# and will return 0 (zero) if the arguments doesn't pass

	# Get the numbers of first and second matrix's row and column
	f_rows = len(f_matrix)
	f_cols = len(f_matrix[0])
	s_rows = len(s_matrix)
	s_cols = len(s_matrix[0])

	# Create the result matrix
	result = init_m(f_rows, s_cols)

	# Make sure that the multipication operation meets the mandatory requirement
	if f_cols == s_rows:
		# Calculate the multiplication
		for i in range(f_rows):
			for j in range(s_cols):
				for k in range(s_rows):
					result[i][j] += f_matrix[i][k] * s_matrix[k][j]

		return result
	else:
		return result

def m_add(f_matrix, s_matrix):
	# This function will adds two matrices.
	# and will return the result matix if the arguments pass the checking process
	# and will return 0 (zero) if the arguments doesn't pass

	# Get the numbers of first and second matrix's row and column
	f_rows = len(f_matrix)
	f_cols = len(f_matrix[0])
	s_rows = len(s_matrix)
	s_cols = len(s_matrix[0])

	# Create the result matrix
	result = init_m(f_rows, s_cols)

	if f_cols == s_cols and f_rows == s_rows:
		for i in range(f_rows):
			for j in range(f_cols):
				result[i][j] += f_matrix[i][j] + s_matrix[i][j]

		return result
	else:
		return result

def m_substract(f_matrix, s_matrix):
	# This function will substracts two matrices.
	# and will return the result matix if the arguments pass the checking process
	# and will return 0 (zero) if the arguments doesn't pass

	# Get the numbers of first and second matrix's row and column
	f_rows = len(f_matrix)
	f_cols = len(f_matrix[0])
	s_rows = len(s_matrix)
	s_cols = len(s_matrix[0])

	# Create the result matrix
	result = init_m(f_rows, f_cols)

	if f_cols == s_cols and f_rows == s_rows:
		for i in range(f_rows):
			for j in range(f_cols):
				result[i][j] = f_matrix[i][j] - s_matrix[i][j]

		return result
	else:
		return result

def m_identity(matrix):
	# This function will return the identity matrix
	# of the matrix from the argument of this function
	row = len(matrix)

	for i in range(row):
		matrix[i][i] = 1

	return matrix

def m_determinant(matrix):
	return matrix