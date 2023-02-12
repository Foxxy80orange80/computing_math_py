#pip install -r lab-1-requirements.txt

#Вариант 11
# Метод Гаусса с выбором главного элемента по столбцам

# Задачи:
# • Вычисление определителя
# • Вывод треугольной матрицы (включая преобразованный столбец В)
# • Вывод вектора неизвестных: 𝑥1, 𝑥2, … , 𝑥𝑛
# • Вывод вектора невязок: 𝑟1, 𝑟, … , 𝑟n

# Условия:
#+++ Размерность матрицы n<=20
#+++ Должна быть реализована возможность ввода коэффициентов матрицы, как с клавиатуры, так и из файла
from art import *
import re
import numpy as np

def log(*args):
    print("\nLOGGER: ",args)


def get_matrix_size():
    while True:
        matrix_size=input("Enter matrix size(row x col, max - 20x20): ")
        log(f"Matrix size is {matrix_size}")
        
        regex_matrix_size=r"\b([1-9]|1\d|20)x([1-9]|1\d|20)\b"

        result = re.fullmatch(regex_matrix_size,matrix_size)
  
        if not result:
            print("\nThis is not a correct answer. Please try again\n")
            
        else:
            log(f"Matrix size ({matrix_size}) is correct")
            return matrix_size



def get_free_members(row):
    print("Enter the free members: ")

    free_members=[]

    for j in range(row):    
        while True:
            try:
                free_members.append(float(input()))    
            except ValueError:
                print("\nIncorrect symbol. Please try again:")
                continue
            log("Symbol correct")
            break
    log(f"Free members: {free_members}")
    return free_members
 


def is_matrix_size_from_file_correct(matrix_size):
    regex_matrix_size=r"\b([1-9]|1\d|20)x([1-9]|1\d|20)\b"

    result = re.fullmatch(regex_matrix_size,matrix_size)  
    if not result:
        print("\nThis is not a correct size.\n")   
        return False         
    else:
        log(f"Matrix size ({matrix_size}) is correct") 
    return True



def get_matrix_from_file(path):
    # try:
        with open(path,'r',encoding="UTF-8") as f:
            lines = [line.rstrip() for line in f]
            f.close()

        if is_matrix_size_from_file_correct(lines[0]):
            matrix_size_list=lines[0].split('x')
        else:
            print("Error. Try again")
            return 0
        row=int(matrix_size_list[0])
        col=int(matrix_size_list[1])

        matrix_elements_str=lines[1:(row+col+1)]
        matrix_elements_float=[]
        for i in range(row*col):
            matrix_elements_float.append(float(matrix_elements_str[i]))

        free_members_str=lines[(row+col+1):(row+col*2+2)]
        free_members=[]
        for i in range(row):
            free_members.append(float(free_members_str[i]))

        if row*col+col<len(lines[1:]):
            print("\nNumber of elements is bigger than its size. Not all number will be in your matrix\n")

        count=0

        final_matrix=[]
        for i in range (row):
            my_mas=[]
            for j in range (col):    
                my_mas.append(matrix_elements_float[count])
                count+=1
            final_matrix.append(my_mas)
       
        print_matrix(final_matrix)
        return final_matrix,row,col,free_members
     
    

def get_matrix_from_input():
    matrix_size_list=get_matrix_size().split("x")

    row=int(matrix_size_list[0])
    column=int(matrix_size_list[1])
    matrix = []  
    while True:
        print("Enter the entries row wise: ")  
        for i in range(row):       
            row_massive =[]  
            for j in range(column):    
                while True:
                    try:
                        row_massive.append(float(input()))    
                    except ValueError:
                        print("\nIncorrect symbol. Please try again:")
                        continue
                    log("Symbol correct")
                    break

            matrix.append(row_massive) 

        log(f"Entered matrix: {matrix}")

        return matrix,row,column

def print_matrix(matrix):
     for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j==len(matrix[i])-1:
                print ("| %3.2f" % (matrix[i][j]), end = " ")
            else:    
                print ("%5.2f" % (matrix[i][j]), end = " ")
        print()
 
def join_matrix_free_members(matrix,free_members,row,col):
        final_matrix=[[0]*(col+1) for i in range(row)]
        log(matrix)
        log(final_matrix)

        for i in range (row):
            for j in range (col+1):
                log(j)
                if j==col:
                    final_matrix[i][j]=free_members[i]
                else:    
                    final_matrix[i][j]=(matrix[i][j])

        log(f"Matrix elements: {final_matrix}") 
        return final_matrix
 

def find_determinant():
    pass


def show_triangular_matrix():
    pass


def show_vectors_of_unknowns():
    pass


def show_residual_vectors():
    pass


def main():
    tprint("Gauss   method\n(main element)")
    while True:
        try:
            input_choice=int(input("How do you want to enter the matrix? Press (1) if from keybord or (0) if from a file: "))
            if input_choice==1:
                matrix,row,column=get_matrix_from_input()
                free_members=get_free_members(row)
            if input_choice==0:
                path=input("\nEnter the path to a file: ")
                matrix,row,column,free_members=get_matrix_from_file(path)
                

            matrix_with_free_members= join_matrix_free_members(matrix,free_members,row,column)
            print_matrix(matrix_with_free_members)
            

        except (KeyboardInterrupt,EOFError):
            print("EXIT command\n")
            break
        except FileNotFoundError:
            print("There is no such file. Try again\n")
            continue
        except ValueError:
            print("Input error. Try again\n")    
            continue
    
if __name__=="__main__":
    main()