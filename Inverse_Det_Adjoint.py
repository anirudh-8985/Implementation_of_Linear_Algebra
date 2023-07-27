import copy


def det_mat(matrix):
	x = int(matrix[0][0])*int(matrix[1][1])
	y = int(matrix[0][1])*int(matrix[1][0])
	return(x-y)

def determinant_recursive(matrix,total=0):
    if(m1 == 1):
        val = int(matrix[0][0])
        return val

    elif len(matrix) == 2 and len(matrix[0]) == 2:
        val = det_mat(matrix)
        return val

    for x in range(m1):
        submatrix = matrix
        submatrix = submatrix[1:]
        length = len(submatrix)

        for y in range(length):
            submatrix[y] = submatrix[y][0:x] + submatrix[y][x+1:]

        sign = (-1)**(x%2)

        sub_det = determinant_recursive(submatrix)
        total += sign * int(matrix[0][x]) * sub_det   
        
    return total


def adjoint_mat(matrix):
    adjoint = copy.deepcopy(matrix)

    if(m1 == 1):
        return adjoint

    elif(m1 == 2):
        adjoint[0][0] = matrix[1][1]
        adjoint[0][1] = -int(matrix[0][1])
        adjoint[1][0] = -int(matrix[1][0])
        adjoint[1][1] = matrix[0][0]

        return adjoint

    for x in range(m1):
        for y in range(n1):
            
            a_submatrix = copy.deepcopy(matrix)
            for lst in a_submatrix:
                lst.pop(y)

            a_submatrix.pop(x)

            length = len(a_submatrix)
    
            temp = determinant_recursive(a_submatrix)
            adjoint[y][x] = (-1)**(x+y) * temp

    return adjoint

def inverse_mat(matrix):
    det = determinant_recursive(matrix)
    adjoint = adjoint_mat(matrix)
    inverse = []
    row = []
    for x in range(m1):
        for y in range(n1):
            row.append(int(adjoint[x][y]) / det)
        inverse.append(row)
        row = []


    return inverse


print("Enter the dimensions of a Square Matrix")
m1, n1 = map(int,(input("Enter the value m and n of Matrix1 of size m*n : ").split()))

if(m1 == n1):
    Matrix = [] #Declaration of the matrix
    for x in range(m1):
        print("Enter row",x,"elements of matrix1 : ")
        Matrix.append((list)(input().split()))

    action = int(input("\nEnter:\n 1) For Determinant \n 2) For Adjoint\n 3) For Inverse of the matrix :"))

    if(action == 1):
        det = determinant_recursive(Matrix)
        print("The Determinant of the matrix is : ",det)
    elif(action == 2):
        adjoint = adjoint_mat(Matrix)
        print("The Adjoint of the matrix is : ",adjoint)

    elif(action == 3):
        inverse = inverse_mat(Matrix)
        print("The Inverse of the matrix is : ",inverse)

    elif(action>3 or action<1):
        print("Incorrect Input")

elif(m1 != n1):
    print("***** Computations are only possible for Square Matrix *****")
