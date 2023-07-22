# Martix Matrix addition, subtraction and multiplication without using any library function in python3

m1, n1 = map(int,(input("Enter the value m and n of Matrix1 of size m*n : ").split()))

Matrix1 = []
for x in range(m1):
	print("Enter row",x,"elements of matrix1 : ")
	Matrix1.append((list)(input().split()))

m2, n2 = map(int,(input("Enter the value m and n of Matrix2 of size m*n : ").split()))

Matrix2 = []
for x in range(m2):
	print("Enter row",x,"elements of Matrix2 : ")
	Matrix2.append((list)(input().split()))

action = int(input("\nEnter:\n 1) For additon\n 2) For Subtraction\n 3) For Multiplication of the matrices :"))

Matrix3 = []
list1 = []
if(action == 1) :
	if(m1==m2 and n1==n2):
		for x in range(m1):
			for y in range(n1):
				list1.append(int(Matrix1[x][y]) + int(Matrix2[x][y]))
			Matrix3.append(list1)
			list1 = []
	print(Matrix3)

if(action == 2) :
	if(m1==m2 and n1==n2):
		for x in range(m1):
			for y in range(n1):
				list1.append(int(Matrix1[x][y]) - int(Matrix2[x][y]))
			Matrix3.append(list1)
			list1 = []
	print(Matrix3)


temp = 0
if (action == 3):
	if(n1==m2):
		for i in range(m1):
			for j in range(n2):
				for k in range(n2):
					temp += (int(Matrix1[i][k]) * int(Matrix2[k][j]))
				list1.append(temp)
				temp = 0
			Matrix3.append(list1)
			list1 = []
	print(Matrix3)

