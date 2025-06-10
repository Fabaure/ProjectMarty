from math import floor
import re

def createMatrix(dimension):
    matrix = []
    mid = floor(dimension/2)
    for i in range(dimension): # creating the matrix
        row = []
        for j in range(dimension):
            row.append(0)
        matrix.append(row)  # adding rows to the matrix

    for i in range(dimension): # show the matrix in terminal
        for j in range(dimension):
            if(mid == i and mid == j):
                matrix[i][j] = 1
    return matrix

def afficherMatrix(matrix):
        for i in range(len(matrix)): # show the matrix in terminal
            for j in range(len(matrix)):
                print(matrix[i][j], end=" ")
            print()

def sequential(dimension):
    dance_steps,dance_direction = lecture()
    print("Nb de pas")
    print(dance_steps)
    print("Direction")
    print(dance_direction)
    matrix = createMatrix(dimension)
    afficherMatrix(matrix)

    
    for i in range(len(dance_direction)):
        steps = int(dance_steps[i]) * 2
        match dance_direction[i]:
            case "L":
                move = MoveL(matrix,dimension,int(dance_steps[i]))
                if(move!=False):
                    print(dance_steps[i]+"L")
                    afficherMatrix(matrix)
            case "R":
                move = MoveR(matrix,dimension,int(dance_steps[i]))
                if(move!=False):
                    print(dance_steps[i]+"R")
                    afficherMatrix(matrix)
            case "U":
                move = MoveU(matrix,dimension,int(dance_steps[i]))
                if(move!=False):
                    print(dance_steps[i]+"U")
                    afficherMatrix(matrix)
            case "B":
                move = MoveB(matrix,dimension,int(dance_steps[i]))
                if(move!=False):
                    print(dance_steps[i]+"B")
                    afficherMatrix(matrix)

def lecture():
    dance = open('dominance.dance', 'r')
    contenu_dance = dance.read()
    tab_dance = re.split(r'[ \n]+', contenu_dance)
    print(tab_dance)
    dance.close()

    if(tab_dance[0] == "SEQ"): # if in absolute mode
        dance_steps = []
        dance_direction = []
        for i in range(2, len(tab_dance)): # disassemble the original table
            dance_steps.append(tab_dance[i][0]) # table with the number of steps
            dance_direction.append(tab_dance[i][1])
        return dance_steps,dance_direction

def MoveL(matrix, dimension,dance_steps):
    for i in range(dimension): # show the matrix in terminal
        for j in range(dimension):
            if(matrix[i][j]==1 and j>(dance_steps-1)):
                matrix[i][j] = 0
                matrix[i][j-dance_steps] = 1
                return matrix
            elif(matrix[i][j]==1 and j<=(dance_steps-1)):
                print("Out of range")
                return False

def MoveR(matrix, dimension,dance_steps):
    for i in range(dimension): # show the matrix in terminal
        for j in range(dimension):
            if(matrix[i][j]==1 and j<(3-dance_steps)):
                matrix[i][j] = 0
                matrix[i][j+dance_steps] = 1
                return matrix
            elif(matrix[i][j]==1 and j>=(3-dance_steps)):
                print("Out of range")
                return False

def MoveU(matrix, dimension,dance_steps):
    for i in range(dimension): # show the matrix in terminal
        for j in range(dimension):
            if(matrix[i][j]==1 and i>(dance_steps-1)):
                matrix[i][j] = 0
                matrix[i-dance_steps][j] = 1
                return matrix
            elif(matrix[i][j]==1 and i<=(dance_steps-1)):
                print("Out of range")
                return False

def MoveB(matrix,dimension,dance_steps):
    for i in range(dimension): # show the matrix in terminal
        for j in range(dimension):
            if(matrix[i][j]==1 and i<(3-dance_steps)):
                matrix[i][j] = 0
                matrix[i+dance_steps][j] = 1
                return matrix
            elif(matrix[i][j]==1 and i>=(3-dance_steps)):
                print("Out of range")
                return False


sequential(3)