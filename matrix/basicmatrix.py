r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

matrix = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    matrix.append(row)


# Print the original matrix
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end="")
    print()  

# Print the transpose of the matrix
for j in range(c):
    for i in range(r):
        print(matrix[i][j],end="")
    print()    

# Print diaginal elements of the matrix

for i in range(r):   
    print(matrix[i][i],end="")

# print Secondary diagonal elements of the matrix
for i in range(r):
    print(matrix[i][r-1-i],end="")

# Directions of the matrix

directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up

for dr , dc in directions:
    nr = r + dr
    nc = c + dc


                 
