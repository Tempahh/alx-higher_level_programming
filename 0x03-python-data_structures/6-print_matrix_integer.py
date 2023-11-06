#!/Users/mac/opt/anaconda3/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for columns in row:
            print("{:4}" .format(columns), end='')
        print()
