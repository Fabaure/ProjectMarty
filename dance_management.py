from math import floor
import re
from feel_management import *
from movement import *

def createMatrix(dimension):
    # function to create a matrix depending on the input size and placing the robot in the center
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
        # function to show the matrix in terminal
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j], end=" ")
            print()

def sequential(marty, dance_steps, dance_direction, dimension):
    # function called if we are using the sequential mode to pilot the robot
    feels_color, feels_mood, feels_colorhex = lectureFichierFeel(marty)
    print("Nb de pas")
    print(dance_steps)
    print("Direction")
    print(dance_direction)
    matrix = createMatrix(dimension)
    afficherMatrix(matrix)
    
    for i in range(len(dance_direction)):
        steps = int(dance_steps[i])
        emotions(marty, feels_color, feels_mood, feels_colorhex)
        match dance_direction[i]:
            case "L":
                # if the robot is moving left
                move = MoveL(matrix,dimension,int(dance_steps[i]))
                if(move!=False):
                    print(dance_steps[i]+"L")
                    afficherMatrix(matrix)
                    move_left(marty, steps*6)
            case "R":
                # if the robot is moving right
                move = MoveR(matrix,dimension,int(dance_steps[i]))
                if(move!=False):
                    print(dance_steps[i]+"R")
                    afficherMatrix(matrix)
                    move_right(marty, steps*6)
            case "U":
                # if the robot is moving forwards
                move = MoveU(matrix,dimension,int(dance_steps[i]))
                if(move!=False):
                    print(dance_steps[i]+"U")
                    afficherMatrix(matrix)
                    move_forward(marty, steps*5)
            case "B":
                # if the robot is moving backwards
                move = MoveB(matrix,dimension,int(dance_steps[i]))
                if(move!=False):
                    print(dance_steps[i]+"B")
                    afficherMatrix(matrix)
                    move_backward(marty, steps*5)
            case _:
                print("error : pas une bonne lettre en entrée.")

def lectureFichierDance(marty):
    # function to read the file .dance
    dance = open('../dominance.dance', 'r')
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
        sequential(marty, dance_steps, dance_direction, int(tab_dance[1]))

def MoveL(matrix, dimension,dance_steps):
    # function to move left in the matrix and verify if it's possible (not going outside of the matrix)
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
    # function to move right in the matrix and verify if it's possible (not going outside of the matrix)
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
    # function to move forward in the matrix and verify if it's possible (not going outside of the matrix)
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
    # function to move backwards in the matrix and verify if it's possible (not going outside of the matrix)
    for i in range(dimension): # show the matrix in terminal
        for j in range(dimension):
            if(matrix[i][j]==1 and i<(3-dance_steps)):
                matrix[i][j] = 0
                matrix[i+dance_steps][j] = 1
                return matrix
            elif(matrix[i][j]==1 and i>=(3-dance_steps)):
                print("Out of range")
                return False