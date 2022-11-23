import numpy as np
import sys

def lu(X, n):

    L = [[0.00] * n for i in range(n)]
    L = np.round_(L, decimals=4)
    U = np.copy(X)
    for eli in range(n):
        temp_ul(U , L, n, eli)

    return L, U

def temp_ul(A, L, n, el):
    # where is pivot position
    elx = el
    ely = el
    nonZeroColumn = False
    if A[el][el] == 0:
        for p in range(n):
            if el+p<n and A[el+p][el] != 0:
                nonZeroColumn = True
                for t in range(n):
                    tmp = A[el+p][t]
                    A[el+p][t] = A[el][t]
                    A[el][t] = tmp
        if  not nonZeroColumn:
            for z in range(n):
                
                if el + 1 < n and A[z][el+1] != 0:
                    elx = z
                    ely = el+1
   
    # L matrix
    U = A
    for j in range(n):
        if j + elx < n and U[elx][j+ely] != 0:
            L[j+elx][ely] = U[j+elx][ely] / U[elx][ely]

    # U matrix
    for i in range(elx+1, n):
        x = float(A[i][ely] / A[elx][ely])
        A[i][ely] = A[i][ely] - x * (A[elx][ely])
        for k in range(elx+1, n):
            A[i][k] = A[i][k] - x * A[elx][k]

    return A

    
inp = input().split(" ")
n = int(inp[0])
m = int(inp[1])

A =  np.empty([n, n])
for i in range(n):
    array = input().split(" ")
    for j in range(n):
         A[i][j] = int(array[j])
    
b = np.empty([n, 1])
x = np.empty([n, 1])
np.round_(x, decimals=3)
answer = " "
for i in range(m):
    inpp = input().split(" ")
    for j in range(n):
         b[j][0] = int(inpp[j])
    b = np.reshape(b, (-1, 1))
    L, U = lu(A, len(A))
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    np.round_(x, 3)
    np.around(x, 3)

    for row in x:
        answer += " ".join(map(str, row.tolist())) + " " 
    answer += "\n"
    
print(answer)
