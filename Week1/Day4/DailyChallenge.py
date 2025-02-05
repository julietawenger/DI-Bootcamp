"""
Matrix  
7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r! 

To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

Using his technique, try to decode this matrix.

"""
alphabet = [chr(i) for i in range(97, 123)] + [chr(i).capitalize() for i in range(97, 123)]
matrix_string = "7ii,Tsx,h%?,i #,sM ,$a ,#t%,^r!" 
matrix = [list(x) for x in matrix_string.split(",")]
for j in range (len(matrix[0])):
    for i in range(len(matrix)):
        if matrix[i][j] in alphabet:
            print(matrix[i][j]) 
        else:
            print(' ')    