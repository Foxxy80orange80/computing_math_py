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
    
        log(f"Matrix size: {lines[0]}")
        log(f"Matrix elements: {lines[1:]}")
        if is_matrix_size_from_file_correct(lines[0]):
            matrix_size_list=lines[0].split('x')
        else:
            print("Error. Try again")
            return 0
        row=int(matrix_size_list[0])
        col=int(matrix_size_list[1])
        log(f"Row: {row}")
        log(f"Col: {col}")
        
        

        matrix_elements_str=lines[1:(row+col+1)]
        matrix_elements_int=[]
        for i in range(row*col):
            matrix_elements_int.append(float(matrix_elements_str[i]))

        free_members_str=lines[(row+col+1):(row+col*2+2)]
        free_members=[]
        for i in range(row):
            free_members.append(float(free_members_str[i]))
        log(f"Free members: {free_members}")

        # !!
        log(f"Expected size: {row*col+col}")
        log(f"Matrix elements count: {len(matrix_elements_int)}")
        log(f"Free members count:{len(free_members)} ")
        if row*col+col<len(lines[1:]):
            print("\nNumber of elements is bigger than its size. Not all number will be in your matrix\n")
                   
        final_matrix=[[0]*(col+1) for i in range(row)]
        count=0
        for i in range (row):
            for j in range (col+1):
                if j==col:
                    final_matrix[i][j]=free_members[i]
                else:    
                    final_matrix[i][j]=matrix_elements_int[count]
                    count+=1
        log(f"Matrix elements: {final_matrix}")                        
        print("Your matrix looks like this: ")       
        for i in range(row):  
            for j in range(col+1):  
                if j==col:
                    print(" | %7.2f" %(final_matrix[i][j]), end=" ")  
                else:
                    print("%7.2f" %(final_matrix[i][j]), end=" ")  
            print()          
        return final_matrix
    # except (ValueError,IndexError) as e:
    #     print("Invalid data. Change your file\n")
        
    #     return 0       
    

def get_matrix_from_input():
    matrix_size_list=get_matrix_size().split("x")
    log(f"Matrix size after split: {matrix_size_list}")

    row=int(matrix_size_list[0])
    column=int(matrix_size_list[1])
    
    matrix = []  
    free_members=get_free_members(row)
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
            row_massive.append(free_members[i])
            matrix.append(row_massive) 
        
        log(f"Free members: {free_members}")
        log(f"Entered matrix: {matrix}")
        print("\nYour matrix looks like this:")
        for i in range(row):  
            for j in range(column+1):   
                if j==column:
                    print("  | %6.2f" %(matrix[i][j]), end=" ")  
                else:
                    print("%7.2f" %(matrix[i][j]), end=" ")  

            print()
        
        
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
            input_choice=int(input("How do you want to enter the matrix? Press (1) if from keybord or (0) if from a file: "))
            if input_choice:
                get_matrix_from_input()
            elif not input_choice:
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