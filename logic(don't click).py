w, h = 3, 3
Matrix = [[0 for x in range(w)] for y in range(h)]
w, h = 0,0
WIDTH = 3
LENGTH = 3
P1Turn = True
st = 0
while(True):
    st = input()
    if(P1Turn):
        if(st=='q'):
            if(Matrix[0][0] == 0):
                Matrix[0][0] = 1
                P1Turn = False
        elif(st=='w'):
            if(Matrix[0][1] == 0):
                Matrix[0][1] = 1
                P1Turn = False
        elif(st=='e'):
            if(Matrix[0][2] == 0):
                Matrix[0][2] = 1
                P1Turn = False
        elif(st=='a'):
            if(Matrix[1][0] == 0):
                Matrix[1][0] = 1
                P1Turn = False
        elif(st=='s'):
            if(Matrix[1][1] == 0):
                Matrix[1][1] = 1
                P1Turn = False
        elif(st=='d'):
            if(Matrix[1][2] == 0):
                Matrix[1][2] = 1
                P1Turn = False
        elif(st=='z'):
            if(Matrix[2][0] == 0):
                Matrix[2][0] = 1
                P1Turn = False
        elif(st=='x'):
            if(Matrix[2][1] == 0):
                Matrix[2][1] = 1
                P1Turn = False
        elif(st=='c'):
            if(Matrix[2][2] == 0):
                Matrix[2][2] = 1
                P1Turn = False
    if(P1Turn == False):
        if(st=='u'):
            if(Matrix[0][0] == 0):
                Matrix[0][0] = 2
                P1Turn = True
        elif(st=='i'):
            if(Matrix[0][1] == 0):
                Matrix[0][1] = 2
                P1Turn = True
        elif(st=='o'):
            if(Matrix[0][2] == 0):
                Matrix[0][2] = 2
                P1Turn = True
        elif(st=='h'):
            if(Matrix[1][0] == 0):
                Matrix[1][0] = 2
                P1Turn = True
        elif(st=='j'):
            if(Matrix[1][1] == 0):
                Matrix[1][1] = 2
                P1Turn = True
        elif(st=='k'):
            if(Matrix[1][2] == 0):
                Matrix[1][2] = 2
                P1Turn = True
        elif(st=='b'):
            if(Matrix[2][0] == 0):
                Matrix[2][0] = 2
                P1Turn = True
        elif(st=='n'):
            if(Matrix[2][1] == 0):
                Matrix[2][1] = 2
                P1Turn = True
        elif(st=='m'):
            if(Matrix[2][2] == 0):
                Matrix[2][2] = 2
                P1Turn = True
    i = 0
    for i in range (3):
        j = 0
        for j in range(3):
            if(Matrix[i][j] == 0):
                print("o ")
            else:
                print("x ")
    print("\n")

    if(Matrix[0][0] == 1 and Matrix[0][1] == 1 and Matrix[0][2] == 1):
        print("Player 1 wins")
    if(Matrix[1][0] == 1 and Matrix[1][1] == 1 and Matrix[1][2] == 1):
        print("Player 1 wins")
    if(Matrix[2][0] == 1 and Matrix[2][1] == 1 and Matrix[2][2] == 1):
        print("Player 1 wins")
    if(Matrix[0][0] == 1 and Matrix[1][0] == 1 and Matrix[2][0] == 1):
        print("Player 1 wins")
    if(Matrix[0][1] == 1 and Matrix[1][1] == 1 and Matrix[2][1] == 1):
        print("Player 1 wins")
    if(Matrix[0][2] == 1 and Matrix[1][2] == 1 and Matrix[2][2] == 1):
        print("Player 1 wins")
    if(Matrix[0][0] == 1 and Matrix[1][1] == 1 and Matrix[2][2] == 1):
        print("Player 1 wins")
    if(Matrix[0][2] == 1 and Matrix[1][1] == 1 and Matrix[2][0] == 1):
        print("Player 1 wins")

    if(Matrix[0][0] == 2 and Matrix[0][1] == 2 and Matrix[0][2] == 2):
        print("Player 2 wins")
    if(Matrix[1][0] == 2 and Matrix[1][1] == 2 and Matrix[1][2] == 2):
        print("Player 2 wins")
    if(Matrix[2][0] == 2 and Matrix[2][1] == 2 and Matrix[2][2] == 2):
        print("Player 2 wins")
    if(Matrix[0][0] == 2 and Matrix[1][0] == 2 and Matrix[2][0] == 2):
        print("Player 2 wins")
    if(Matrix[0][1] == 2 and Matrix[1][1] == 2 and Matrix[2][1] == 2):
        print("Player 2 wins")
    if(Matrix[0][2] == 2 and Matrix[1][2] == 2 and Matrix[2][2] == 2):
        print("Player 2 wins")
    if(Matrix[0][0] == 2 and Matrix[1][1] == 2 and Matrix[2][2] == 2):
        print("Player 2 wins")
    if(Matrix[0][2] == 2 and Matrix[1][1] == 2 and Matrix[2][0] == 2):
        print("Player 2 wins")
