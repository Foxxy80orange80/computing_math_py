import numpy as np

# matrix_with_free_members
A = [[3.25, 1.54, 2.91, 5.43, 4.14],
    [7.13, 8.21, 4.47, -2.11,5.65], 
    [ 4.52, 6.73, 1.37, -9.89, 2.92], 
    [-6.34, -8.17, -10.2, 3.93, 3.15]]
# free_members
B = [4.14, 5.65, 2.92, 3.15]
# matrix
C = [[3.25, 1.54, 2.91, 5.43],
    [7.13, 8.21, 4.47, -2.11], 
    [ 4.52, 6.73, 1.37, -9.89], 
    [ -6.34, -8.17, -10.2, 3.93]]
    
    # null_matrix_of_free_members
x = np.zeros((4, 1))
 
def print_matrix(matrix):
     for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print ("%2.4f" % (matrix[i][j]), end = ' ')
        print()
 
def matrix_max_row(matrix, n):
    max_element = matrix[n][n]
    max_row = n
    for i in range(n + 1, len(matrix)):
        if abs(matrix[n][i]) > abs(max_element):
            max_element = matrix[n][i]
            max_row = i
        if max_row != n:
            matrix[n], matrix[max_row] = matrix[max_row], matrix[n]
        #print(matrix, max_element, max_row)
        #print('/n')
 
 
def Gauss(matrix):
    n = len(matrix)
    for k in range(n - 1):
        matrix_max_row(matrix, k)
        for i in range(k + 1, n):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]
            for j in range(k, n):
                matrix[i][j] -= div * matrix[k][j]
    if is_singular(matrix):
        print('Система имеет бесконечное число решений')
        return
    # Обратный ход
    for k in range(n - 1, -1, -1):
        x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, n) ])) / matrix[k][k]
    return x
 
def Gauss_print(x, matrix):
    det = 1.0
    print("Решение методом Гауса: ")
    for k in range(len(x)):
        print('x[', k + 1, '] =', "%2.4f" % (x[k]), end = '\n')
    print(" ")
    print('A:')
    print_matrix(matrix)
    for i in range(len(C)):
        det *=  A[i][i]
    det = abs(det)
    print(" ")
    print("Определитель:", det)
    return x
 
def is_singular(matrix):
    for i in range(len(matrix)):
        if not matrix[i][i]:
            return True
        return False
 
def nevyazka():
    temp = np.zeros((4, 1))
    r = np.zeros((4, 1))
    print('Вектор невязки:')
    for i in range(len(C)):
        temp[i] = 0
        for j in range(len(C)):
            temp[i] += x[j] * C[i][j]
        r[i] = temp[i] - B[i]
        print('r[', i + 1, '] =', "%.12f" % (r[i]), end = '\n')


def inverse(C, n):
    D = np.eye(n)
    inv = np.zeros((n, n))
    xinv = np.zeros((n, 1))
    temp = np.zeros((n, n))
    temp1 = np.zeros((n, 1))
    for l in range(n):
        for i in range(n):
            for j in range(n):
                temp[i][j] = C[i][j]
            temp1[i] = D[i][l]
        i = 0
        j = 0
        m = np.column_stack((temp, temp1))#склелилa матрицу и вектор 
        # Прямой ход
        for k in range(n):
            swap_row = pick_nonzero_row(m, k)
            if swap_row != k:
                m[k, :], m[swap_row, :] = m[swap_row, :], np.copy(m[k, :])
            if m[k, k] != 1:
                m[k, :] *= 1 / m[k, k]
            for row in range(k + 1, n):
                m[row, :] -= m[k, :] * m[row, k]
        # Обратный ход
        for k in range(n - 1, 0, -1):
            for row in range(k - 1, -1, -1):
                if m[row, k]:
                    m[row, :] -= m[k, :] * m[row, k]
        xinv = np.hsplit(m,  5)[4]#разклелилa матрицу и вектор 
        i = 0
        for i in range(n):
            inv[i, l] = xinv[i]
    print("Обратная матрица: ")
    print_matrix(inv)
    print(" ")
    #проверка нa правильность решения
    Z = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][k] += C[i][j] * inv[j][k]
    print("Проверка обратной матрицы: ")
    print_matrix(abs(Z))        
    
def pick_nonzero_row(m, k):
    while k < m.shape[0] and not m[k, k]:
        k += 1
    return k
 
Gauss(A)
Gauss_print(x, A)
print('')
nevyazka()
print('')
inverse(C, len(C))
del A, B, C
