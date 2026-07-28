def read_matrix(rows, cols, name="Matrix"):
    """Reads a matrix from user input row by row."""
    matrix = []
    print(f"\nEntering {name} ({rows}x{cols}):")
    for i in range(rows):
        row_str = input(f"Enter row {i + 1}: ")
        row = [int(val) for val in row_str.strip().split()]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Prints a matrix in a neat, aligned grid format."""
    for row in matrix:
        print(" ".join(f"{val:>4}" for val in row))


def transpose_matrix(matrix):
    """Computes the transpose of a matrix (M x N -> N x M)."""
    rows = len(matrix)
    cols = len(matrix[0])
    
  
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
        
    return transposed


def add_matrices(matrix_a, matrix_b):
    """Computes element-wise sum of two M x N matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
        
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Computes the matrix product A x B (M x N multiplied by N x P = M x P)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            row.append(dot_product)
        result.append(row)
        
    return result


def main():
    print("=== PART A: Transpose Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix_a = read_matrix(m, n, "Original Matrix")
    
    print("\nOriginal Matrix:")
    print_matrix(matrix_a)
    
    transposed = transpose_matrix(matrix_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    print("\n" + "="*40)
    print("=== PART B: Add Two Matrices ===")
    print(f"Reading second matrix of size {m}x{n} for addition...")
    matrix_b = read_matrix(m, n, "Matrix B")
    
    sum_matrix = add_matrices(matrix_a, matrix_b)
    print("\nMatrix A + Matrix B:")
    print_matrix(sum_matrix)

    print("\n" + "="*40)
    print("=== PART C: Multiply Two Matrices ===")
    p = int(input(f"Enter number of columns for Matrix C (Matrix A is {m}x{n}, Matrix C will be {n}xP): "))
    matrix_c = read_matrix(n, p, "Matrix C")
    
    product_matrix = multiply_matrices(matrix_a, matrix_c)
    print("\nMatrix A x Matrix C:")
    print_matrix(product_matrix)


if __name__ == "__main__":
    main()
