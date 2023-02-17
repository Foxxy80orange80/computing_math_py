#pip install -r lab-1-requirements.txt

#Вариант 11
# Метод Гаусса с выбором главного элемента по столбцам

# Задачи:
# +++ Вычисление определителя
# +++ Вывод треугольной матрицы (включая преобразованный столбец В)
# • Вывод вектора неизвестных: 𝑥1, 𝑥2, … , 𝑥𝑛
# +++ Вывод вектора невязок: 𝑟1, 𝑟, … , 𝑟n

# Условия:
# +++ Размерность матрицы n<=20
# +++ Должна быть реализована возможность ввода коэффициентов матрицы, как с клавиатуры, так и из файла

# ТЕСТЫ: 
#       test1.txt - матрица 4х4, без ошибок
#       test2.txt - матрица 2х2, без ошибок, больше элементов, чем нужно
#       test3.txt - матрица 2х2, недостаточно элементов
#       test4.txt - полностью пустой файл
#       test5.txt - матрица 2х2, недопустимые символы

from art import *
import re
import numpy as np

def log(*args):
    print("\nLOGGER: ",args)


def get_matrix_size():
    while True:
        matrix_size=input("Введите размер матрицы(строка х колонка , max - 20x20): ")
        
        regex_matrix_size=r"\b([1-9]|1\d|20)x([1-9]|1\d|20)\b"

        result = re.fullmatch(regex_matrix_size,matrix_size)
  
        if not result:
            print("\nНеправильный формат размера. Попробуйте еще раз\n")
            
        else:
            return matrix_size



def get_free_members(row):
    print("Введите свободные члены: ")

    free_members=[]

    for j in range(row):    
        while True:
            try:
                free_members.append(float(input()))    
            except ValueError:
                print("Недопустимый символ. Попробуйте еще раз:")
                continue
            break
    return free_members
 


def is_matrix_size_from_file_correct(matrix_size):
    regex_matrix_size=r"\b([1-9]|1\d|20)x([1-9]|1\d|20)\b"

    result = re.fullmatch(regex_matrix_size,matrix_size)  
    if not result:
        print("\nНеправильный формат размера.\n")   
        return False         
    return True



def get_matrix_from_file(path):
   
        with open(path,'r',encoding="UTF-8") as f:
            lines = [line.rstrip() for line in f]
            f.close()

        if is_matrix_size_from_file_correct(lines[0]):
            matrix_size_list=lines[0].split('x')
        else:
            print("Не удалось выделить размер.")
            return 0
        row=int(matrix_size_list[0])
        col=int(matrix_size_list[1])

        matrix_elements_str=lines[1:(row*col+1)]
        
        matrix_elements_float=[]
        for i in range(len(matrix_elements_str)):
            matrix_elements_float.append(float(matrix_elements_str[i]))
        free_members_str=lines[(row*col+1):(row*col*2+2)]
        free_members=[]
        for i in range(row):
            free_members.append(float(free_members_str[i]))

        if row*col+col<len(lines[1:]):
            print("\nКоличество элементов больше заданного размера. Не все числа попадут в конечную матрицу\n")

        count=0

        final_matrix=[]
        for i in range (row):
            my_mas=[]
            for j in range (col):    
                my_mas.append(matrix_elements_float[count])
                count+=1
            final_matrix.append(my_mas)
        return final_matrix,row,col,free_members
     
    

def get_matrix_from_input():
    matrix_size_list=get_matrix_size().split("x")

    row=int(matrix_size_list[0])
    column=int(matrix_size_list[1])
    matrix = []  
    while True:
        print("\nВведите элементы матрицы построчно: ")  
        for i in range(row):       
            row_massive =[]  
            for j in range(column):    
                while True:
                    try:
                        row_massive.append(float(input()))    
                    except ValueError:
                        print("\nНедопустимый символ. Попробуйте еще раз:")
                        continue
                    break
            matrix.append(row_massive) 
        return matrix,row,column

def print_matrix(matrix):
     for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j==len(matrix[i])-1:
                print ("| %5.2f" % (matrix[i][j]), end = " ")
            else:    
                print ("%7.2f" % (matrix[i][j]), end = " ")
        print()
 
def join_matrix_free_members(matrix,free_members,row,col):
        final_matrix=[[0]*(col+1) for i in range(row)]
        for i in range (row):
            for j in range (col+1):
                # log(j)
                if j==col:
                    final_matrix[i][j]=free_members[i]
                else:    
                    final_matrix[i][j]=(matrix[i][j])
        return final_matrix
 


def matrix_max_row(matrix, col,h):
    replace_count=0
    max_element = matrix[col][col]
    max_row = col
    for i in range(col + 1, len(matrix)):
        if abs(matrix[i][col]) > abs(max_element):
            max_element = matrix[i][col]
            max_row = i
    print(f"Максимальный по модулю элемент {h} столбца равен %.2f" % max_element)
    # переставление строк
    if max_row != col:
        matrix[col], matrix[max_row] = matrix[max_row], matrix[col]
        replace_count+=1
        print(f"Матрица после перестановки {col+1} и {max_row+1} строк:")
    else:
        print("Перестановка не нужна")
    print_matrix(matrix)
    return replace_count

 
 
def Gauss(matrix_with_free_members,x):
    try:
        n = len(matrix_with_free_members)
        h=1
        replace_count=0
        for k in range(n - 1):
            replace_count+=matrix_max_row(matrix_with_free_members, k,h)
            for i in range(k + 1, n):
                div = matrix_with_free_members[i][k] / matrix_with_free_members[k][k]
                # log(f" -1: {matrix_with_free_members[i][-1]}")
                matrix_with_free_members[i][-1] -= div * matrix_with_free_members[k][-1]
                for j in range(k, n):
                    matrix_with_free_members[i][j] -= div * matrix_with_free_members[k][j]
            h+=1
            print("Матрица после преобразования: ")
            print_matrix(matrix_with_free_members)
            print("\n")
            
        for k in range(n - 1, -1, -1):
            x[k] = (matrix_with_free_members[k][-1] - sum([matrix_with_free_members[k][j] * x[j] for j in range(k + 1, n) ])) / matrix_with_free_members[k][k]
        log(f"Количество перестановок: {replace_count}")
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
    return x,matrix_with_free_members,replace_count
 
def Gauss_print(x, matrix_with_free_members,matrix,replace_count,row,free_members):
    det = 1.0
    for i in range(len(matrix)):
        det *=  matrix_with_free_members[i][i]
        # *-1**k, где k- это количество перестановок
    det *= (-1)**replace_count
    if(not det):
        print("Определитель равен 0, нет решений")
        return
    print("Решение методом Гауса: ")
    for k in range(len(x)):
        print('x[', k + 1, '] =', "%2.4f" % (x[k]), end = '\n')
    print(" ")
    print('Вывод треугольной матрицы (включая преобразованный столбец В):')
    print_matrix(matrix_with_free_members)
    
    print(" ")
    print("Определитель:", det)
    nevyazka(x,free_members,matrix,row)
    return x
 

 
def nevyazka(x,free_members,matrix,row):

    result_row = np.zeros((row, 1))
    r = np.zeros((row, 1))
    print('Вектор невязки:')
    for i in range(len(matrix)):
        result_row[i] = 0
        for j in range(len(matrix)):
            result_row[i] += x[j] * matrix[i][j]
        r[i] = result_row[i] - free_members[i]
        print('r[', i + 1, '] =', "%.18f" % (r[i]), end = '\n')


def main():
    tprint("Gauss   method\n(main element)")
    while True:
        try:
            input_choice=int(input("Каким образом ввести элементы матрицы? Нажмите (1), если с клавиатуры, или (0), если из файла: "))
            if input_choice==1:
                matrix,row,column=get_matrix_from_input()
                free_members=get_free_members(row)

            if input_choice==0:
                
                path=input("\nВведите путь к файлу(test1.txt,...,test5.txt): ")
                matrix,row,column,free_members=get_matrix_from_file(path)
                
            matrix_with_free_members= join_matrix_free_members(matrix,free_members,row,column)
            print("\nВаша матрица выглядит так: ")
            print_matrix(matrix_with_free_members)
            print()
            x= np.zeros((row, 1))

            x,matrix_with_free_members,replace_count=Gauss(matrix_with_free_members,x)
            Gauss_print(x, matrix_with_free_members,matrix,replace_count,row,free_members)
            print('')
            del matrix, free_members, matrix_with_free_members

        except (KeyboardInterrupt,EOFError):
            print("ВЫХОД\n")
            break
        except FileNotFoundError:
            print("Такого файла не существует. Попробуйте еще раз\n")
            continue
        except ValueError:
            print("Ошибка ввода. Возможно ошибка внутри файла(если, вы вводили его). Попробуйте еще раз\n")    
            continue
        except IndexError:
            print("\nПустой файл\n")
            continue
        except UnboundLocalError:
            print("Только (1) или (0) !")
            continue
if __name__=="__main__":
    main()