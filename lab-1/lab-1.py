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

def log(*args):
    print("\nLOGGER: ",args)


def get_matrix_size():
    while True:
        matrix_size=input("Enter matrix size(row x col, max - 20x20): ")
        log("Matrix size is "+matrix_size)
        
        regex_matrix_size=r"\b([1-9]|1\d|20)x([1-9]|1\d|20)\b"

        result = re.fullmatch(regex_matrix_size,matrix_size)
  
        if not result:
            print("\nThis is not a correct answer. Please try again\n")
            
        else:
            log("Matrix size ("+matrix_size+") is correct")
            return matrix_size


def is_matrix_size_from_file_correct(matrix_size):
    regex_matrix_size=r"\b([1-9]|1\d|20)x([1-9]|1\d|20)\b"

    result = re.fullmatch(regex_matrix_size,matrix_size)  
    if not result:
        print("\nThis is not a correct size.\n")   
        return False         
    else:
        log("Matrix size ("+matrix_size+") is correct") 
    return True





def get_matrix_from_file(path):
    try:
        with open(path,'r',encoding="UTF-8") as f:
            lines = [line.rstrip() for line in f]
            f.close()
    
        log("Matrix size",lines[0])
        log("Matrix elements",lines[1:])
        if is_matrix_size_from_file_correct(lines[0]):
            matrix_size_list=lines[0].split('x')
        else:
            print("Error. Try again")
            return 0
        row=int(matrix_size_list[0])
        col=int(matrix_size_list[1])
        log("Row",row)
        log("Col",col)
        matrix_elements_str=lines[1:]
        matrix_elements_int=[]
        if row*col<len(matrix_elements_str):
            print("\nNumber of elements is bigger than its size. Not all number will be in your matrix\n")
        for i in range(row*col):
            matrix_elements_int.append(int(matrix_elements_str[i]))            
        final_matrix=[[0]*col for i in range(row)]
        count=0
        for i in range (row):
            for j in range (col):
                final_matrix[i][j]=matrix_elements_int[count]
                count+=1
        log("Matrix elements:",final_matrix)                        
        print("Your matrix looks like this: ")       
        for i in range(row):  
            for j in range(col):  
                print(final_matrix[i][j], end = " ")  
            print()          
        return final_matrix
    except (ValueError,IndexError):
        print("Invalid data. Change your file\n")
        return 0       
    

def get_matrix_from_input():
    matrix_size_list=get_matrix_size().split("x")
    log("Matrix size after split: ",matrix_size_list)

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
                        row_massive.append(int(input()))    
                    except ValueError:
                        print("\nIncorrect symbol. Please try again:")
                        continue
                    log("Fine")
                    break
            matrix.append(row_massive) 

        print("\nYour matrix looks like this:")
        for i in range(row):  
            for j in range(column):  
                print(matrix[i][j], end = " ")  
            print()
        log("Entered matrix: ",matrix)
        return matrix


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
            input_choice=int(input("How do you want to enter the matrix? Press (0) if from keybord or (1) if from a file: "))
            if not input_choice:
                get_matrix_from_input()
            elif input_choice:
                path=input("\nEnter the path to a file: ")
                get_matrix_from_file(path)
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