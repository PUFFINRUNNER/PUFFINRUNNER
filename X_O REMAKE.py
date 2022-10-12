from random import randint
from turtle import*
from math import sqrt
from time import sleep
hideturtle()
speed(0)
a1 = [-100, 100]
a2 = [0, 100]
a3 = [100, 100]
a4 = [-100, 0]
a5 = [0, 0]
a6 = [100, 0]
a7 = [-100, -100]
a8 = [0, -100]
a9 = [100, -100]
b1 = [-125, 100]
b2 = [-125, 0]
b3 = [-125, -100]
b4 = [-100, 125]
b5 = [0, 125]
b6 = [100, 125]
def CROSS():
    left(45)
    pencolor('blue')
    width(2.5)
    forward(100*sqrt(2)/4*3/2)
    penup()
    back(100*sqrt(2)/4*3/2)
    down()
    back(100*sqrt(2)/4*3/2)
    penup()
    forward(100*sqrt(2)/4*3/2)
    down()
    right(90)
    forward(100*sqrt(2)/4*3/2)
    back(100*sqrt(2)/4*3)
    penup()
    goto(-150, 150)
    left(45)
    pencolor('black')
    width(1)
def CIRCLE():
    penup()
    width(2.5)
    pencolor('red')
    left(90)
    back(40)
    right(90)
    down()
    circle(40)
    penup()
    goto(-150, 150)
    pencolor('black')
    width(1)
while True:
    width(1)
    up()
    goto(-150, 150)
    down()
    width(2.5)
    for G in range(4):
        forward(300)
        right(90)
    width(1)
    forward(100)
    right(90)
    forward(300)
    left(90)
    forward(100)
    left(90)
    forward(300)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(300)
    left(90)
    forward(100)
    left(90)
    forward(300)
    back(300)
    left(90)
    forward(200)
    right(90)
    End = 0
    L = [[None, None, None], [None, None, None], [None, None, None]]
    E = int(input('Your move: '))
    if E > 0 and E < 4:
        L[0][E-1] = True
        if E == 1:
            penup()
            goto(a1[0], a1[1])
            down()
            CROSS()
        elif E == 2:
            penup()
            goto(a2[0], a2[1])
            down()
            CROSS()
        elif E == 3:
            penup()
            goto(a3[0], a3[1])
            down()
            CROSS()
    elif E > 3 and E < 7:
        L[1][E-4] = True
        if E == 4:
            penup()
            goto(a4[0], a4[1])
            down()
            CROSS()
        elif E == 5:
            penup()
            goto(a5[0], a5[1])
            down()
            CROSS()
        elif E == 6:
            penup()
            goto(a6[0], a6[1])
            down()
            CROSS()
    elif E > 6 and E < 10:
        L[2][E-7] = True
        if E == 7:
            penup()
            goto(a7[0], a7[1])
            down()
            CROSS()
        elif E == 8:
            penup()
            goto(a8[0], a8[1])
            down()
            CROSS()
        elif E == 9:
            penup()
            goto(a9[0], a9[1])
            down()
            CROSS()
    else:
        print("Please, restart the program")
        exit()

    for Y in range(4):
#######################################################################################################################################################
    
                                           #    XNN
        ADD1 = [L[0][0], L[1][0], L[2][0]] #    XNN
                                           #    XNN
    
                                           #    NXN
        ADD2 = [L[0][1], L[1][1], L[2][1]] #    NXN
                                           #    NXN
                                       
                                           #    NNX
        ADD3 = [L[0][2], L[1][2], L[2][2]] #    NNX
                                           #    NNX
                                       
                                           #    XNN
        ADD4 = [L[0][0], L[1][1], L[2][2]] #    NXN
                                           #    NNX
                                       
                                           #    NNX
        ADD5 = [L[0][2], L[1][1], L[2][0]] #    NXN
                                           #    XNN

#######################################################################################################################################################

        sleep(0.25)
        if True not in L[0] and L[0].count(False) == 2:
            while True:
                O = randint(0, 2)
                if L[0][O] == None:
                    L[0][O] = False
                    if O == 0:
                        penup()
                        goto(a1[0], a1[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a2[0], a2[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a3[0], a3[1])
                        down()
                        CIRCLE()
                    break
        elif True not in L[1] and L[1].count(False) == 2:
            while True:
                O = randint(0, 2)
                if L[1][O] == None:
                    L[1][O] = False
                    if O == 0:
                        penup()
                        goto(a4[0], a4[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a5[0], a5[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a6[0], a6[1])
                        down()
                        CIRCLE()
                    break
        elif True not in L[2] and L[2].count(False) == 2:
            while True:
                O = randint(0, 2)
                if L[2][O] == None:
                    L[2][O] = False
                    if O == 0:
                        penup()
                        goto(a7[0], a7[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a8[0], a8[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a9[0], a9[1])
                        down()
                        CIRCLE()
                    break
        elif True not in ADD1 and ADD1.count(False) == 2:
            while True:
                O = randint(0, 2)
                if L[O][0] == None:
                    L[O][0] = False
                    if O == 0:
                        penup()
                        goto(a1[0], a1[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a4[0], a4[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a7[0], a7[1])
                        down()
                        CIRCLE()
                    break
        elif True not in ADD2 and ADD2.count(False) == 2:
            while True:
                O = randint(0, 2)
                if L[O][1] == None:
                    L[O][1] = False
                    if O == 0:
                        penup()
                        goto(a2[0], a2[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a5[0], a5[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a8[0], a8[1])
                        down()
                        CIRCLE()
                    break
        elif True not in ADD3 and ADD3.count(False) == 2:
            while True:
                O = randint(0, 2)
                if L[O][2] == None:
                    L[O][2] = False
                    if O == 0:
                        penup()
                        goto(a3[0], a3[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a6[0], a6[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a9[0], a9[1])
                        down()
                        CIRCLE()
                    break
        elif True not in ADD4 and ADD4.count(False) == 2:
            while True:
                O = randint(0, 2)
                if L[O][O] == None:
                    L[O][O] = False
                    if O == 0:
                        penup()
                        goto(a1[0], a1[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a5[0], a5[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a9[0], a9[1])
                        down()
                        CIRCLE()
                    break
        elif True not in ADD5 and ADD5.count(False) == 2:
            while True:
                O = randint(0, 2)
                if ADD5[O] == None:
                    if O == 0:
                        L[0][2] = False
                        penup()
                        goto(a3[0], a3[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        L[1][1] = False
                        penup()
                        goto(a5[0], a5[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        L[2][0] = False
                        penup()
                        goto(a7[0], a7[1])
                        down()
                        CIRCLE()           
                    break
        elif False not in L[0] and L[0].count(True) == 2:
            while True:
                O = randint(0, 2)
                if L[0][O] == None:
                    L[0][O] = False
                    if O == 0:
                        penup()
                        goto(a1[0], a1[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a2[0], a2[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a3[0], a3[1])
                        down()
                        CIRCLE()
                    break
        elif False not in L[1] and L[1].count(True) == 2:
            while True:
                O = randint(0, 2)
                if L[1][O] == None:
                    L[1][O] = False
                    if O == 0:
                        penup()
                        goto(a4[0], a4[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a5[0], a5[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a6[0], a6[1])
                        down()
                        CIRCLE()
                    break
        elif False not in L[2] and L[2].count(True) == 2:
            while True:
                O = randint(0, 2)
                if L[2][O] == None:
                    L[2][O] = False
                    if O == 0:
                        penup()
                        goto(a7[0], a7[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a8[0], a8[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a9[0], a9[1])
                        down()
                        CIRCLE()
                    break
        elif False not in ADD1 and ADD1.count(True) == 2:
            while True:
                O = randint(0, 2)
                if L[O][0] == None:
                    L[O][0] = False
                    if O == 0:
                        penup()
                        goto(a1[0], a1[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a4[0], a4[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a7[0], a7[1])
                        down()
                        CIRCLE()
                    break
        elif False not in ADD2 and ADD2.count(True) == 2:
            while True:
                O = randint(0, 2)
                if L[O][1] == None:
                    L[O][1] = False
                    if O == 0:
                        penup()
                        goto(a2[0], a2[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a5[0], a5[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a8[0], a8[1])
                        down()
                        CIRCLE()
                    break
        elif False not in ADD3 and ADD3.count(True) == 2:
            while True:
                O = randint(0, 2)
                if L[O][2] == None:
                    L[O][2] = False
                    if O == 0:
                        penup()
                        goto(a3[0], a3[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a6[0], a6[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a9[0], a9[1])
                        down()
                        CIRCLE()
                    break
        elif False not in ADD4 and ADD4.count(True) == 2:
            while True:
                O = randint(0, 2)
                if L[O][O] == None:
                    L[O][O] = False
                    if O == 0:
                        penup()
                        goto(a1[0], a1[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a5[0], a5[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        penup()
                        goto(a9[0], a9[1])
                        down()
                        CIRCLE()
                    break
        elif False not in ADD5 and ADD5.count(True) == 2:
            while True:
                O = randint(0, 2)
                if ADD5[O] == None:
                    if O == 0:
                        L[0][2] = False
                        penup()
                        goto(a3[0], a3[1])
                        down()
                        CIRCLE()
                    elif O == 1:
                        L[1][1] = False
                        penup()
                        goto(a5[0], a5[1])
                        down()
                        CIRCLE()
                    elif O == 2:
                        L[2][0] = False
                        penup()
                        goto(a7[0], a7[1])
                        down()
                        CIRCLE()           
                    break
        else:
            if True not in L[0]:
                O = randint(0, 2)
                if L[0][O] == None:
                    L[0][O] = False
                    if O == 0:
                        penup()
                        goto(a1[0],a1[1])
                        pendown()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a2[0], a2[1])
                        pendown()
                        CIRCLE()
                    else:
                        penup()
                        goto(a3[0], a3[1])
                        pendown()
                        CIRCLE()
            elif True not in L[1]:
                O = randint(0, 2)
                if L[1][O] == None:
                    L[1][O] = False
                    if O == 0:
                        penup()
                        goto(a4[0],a4[1])
                        pendown()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a5[0], a5[1])
                        pendown()
                        CIRCLE()
                    else:
                        penup()
                        goto(a6[0], a6[1])
                        pendown()
                        CIRCLE()
            elif True not in L[2]:
                O = randint(0, 2)
                if L[2][O] == None:
                    L[2][O] = False
                    if O == 0:
                        penup()
                        goto(a7[0],a7[1])
                        pendown()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a8[0], a8[1])
                        pendown()
                        CIRCLE()
                    else:
                        penup()
                        goto(a9[0], a9[1])
                        pendown()
                        CIRCLE()
            elif True not in ADD1:
                O = randint(0, 2)
                if ADD1[O] == None:
                    L[O][0] = False
                    if O == 0:
                        penup()
                        goto(a1[0],a1[1])
                        pendown()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a4[0], a4[1])
                        pendown()
                        CIRCLE()
                    else:
                        penup()
                        goto(a7[0], a7[1])
                        pendown()
                        CIRCLE()
            elif True not in ADD2:
                O = randint(0, 2)
                if ADD2[O] == None:
                    L[O][1] = False
                    if O == 0:
                        penup()
                        goto(a2[0],a2[1])
                        pendown()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a5[0], a5[1])
                        pendown()
                        CIRCLE()
                    else:
                        penup()
                        goto(a8[0], a8[1])
                        pendown()
                        CIRCLE()
            elif True not in ADD3:
                O = randint(0, 2)
                if ADD2[O] == None:
                    L[O][2] = False
                    if O == 0:
                        penup()
                        goto(a3[0],a3[1])
                        pendown()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a6[0], a6[1])
                        pendown()
                        CIRCLE()
                    else:
                        penup()
                        goto(a9[0], a9[1])
                        pendown()
                        CIRCLE()
            elif True not in ADD4:
                O = randint(0, 2)
                if ADD4[O] == None:
                    L[O][O] = False
                    if O == 0:
                        penup()
                        goto(a1[0],a1[1])
                        pendown()
                        CIRCLE()
                    elif O == 1:
                        penup()
                        goto(a5[0], a5[1])
                        pendown()
                        CIRCLE()
                    else:
                        penup()
                        goto(a9[0], a9[1])
                        pendown()
                        CIRCLE()
            elif True not in ADD5:
                while True:
                    O = randint(0, 2)
                    if ADD5[O] == None:
                        if O == 0:
                            L[0][2] = False
                            penup()
                            goto(a3[0], a3[1])
                            down()
                            CIRCLE()
                        elif O == 1:
                            L[1][1] = False
                            penup()
                            goto(a5[0], a5[1])
                            down()
                            CIRCLE()
                        elif O == 2:
                            L[2][0] = False
                            penup()
                            goto(a7[0], a7[1])
                            down()
                            CIRCLE()           
                        break
            else:
                while True:
                    O = randint(0, 2)
                    P = randint(0, 2)
                    if L[O][P] == None:
                        L[O][P] = False
                        if O == 0 and P == 0:
                            penup()
                            goto(a1[0], a1[1])
                            down()
                            CIRCLE()
                        elif O == 0 and P == 1:
                            penup()
                            goto(a2[0], a2[1])
                            down()
                            CIRCLE()
                        elif O == 0 and P == 2:
                            penup()
                            goto(a3[0], a3[1])
                            down()
                            CIRCLE()
                        elif O == 1 and P == 0:
                            penup()
                            goto(a4[0], a4[1])
                            down()
                            CIRCLE()
                        elif O == 1 and P == 1:
                            penup()
                            goto(a5[0], a5[1])
                            down()
                            CIRCLE()
                        elif O == 1 and P == 2:
                            penup()
                            goto(a6[0], a6[1])
                            down()
                            CIRCLE()
                        elif O == 2 and P == 0:
                            penup()
                            goto(a7[0], a7[1])
                            down()
                            CIRCLE()
                        elif O == 2 and P == 1:
                            penup()
                            goto(a8[0], a8[1])
                            down()
                            CIRCLE()
                        elif O == 2 and P == 2:
                            penup()
                            goto(a9[0], a9[1])
                            down()
                            CIRCLE()
                        break
                

#######################################################################################################################################################

                                           #    XNN
        ADD1 = [L[0][0], L[1][0], L[2][0]] #    XNN
                                           #    XNN
    
                                           #    NXN
        ADD2 = [L[0][1], L[1][1], L[2][1]] #    NXN
                                           #    NXN
                                       
                                           #    NNX
        ADD3 = [L[0][2], L[1][2], L[2][2]] #    NNX
                                           #    NNX
                                       
                                           #    XNN
        ADD4 = [L[0][0], L[1][1], L[2][2]] #    NXN
                                           #    NNX
                                       
                                           #    NNX
        ADD5 = [L[0][2], L[1][1], L[2][0]] #    NXN
                                           #    XNN

#######################################################################################################################################################

        if L[0][0] == True and L[0][1] == True and L[0][2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b1[0], b1[1])
            pendown()
            forward(250)
            break
        elif L[0][0] == False and L[0][1] == False and L[0][2] == False:
            print("PC won!")
            End = 1
            width(5)
            penup()
            goto(b1[0], b1[1])
            pendown()
            forward(250)
            break
        elif L[1][0] == True and L[1][1] == True and L[1][2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b2[0], b2[1])
            pendown()
            forward(250)
            break
        elif L[1][0] == False and L[1][1] == False and L[1][2] == False:
            print("PC won!")
            penup()
            width(5)
            goto(b2[0], b2[1])
            pendown()
            forward(250)
            break
        elif L[2][0] == True and L[2][1] == True and L[2][2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b3[0], b3[1])
            pendown()
            forward(250)
            break
        elif L[2][0] == False and L[2][1] == False and L[2][2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            goto(b3[0], b3[1])
            pendown()
            forward(250)
            break
        elif ADD1[0] == True and ADD1[1] == True and ADD1[2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b4[0], b4[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD1[0] == False and ADD1[1] == False and ADD1[2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            goto(b4[0], b4[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD2[0] == True and ADD2[1] == True and ADD2[2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b5[0], b5[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD2[0] == False and ADD2[1] == False and ADD2[2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            goto(b5[0], b5[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD3[0] == True and ADD3[1] == True and ADD3[2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b6[0], b6[1])
            right(90)
            pendown()
            forward(250)
            break
        elif ADD3[0] == False and ADD3[1] == False and ADD3[2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            goto(b6[0], b6[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD4[0] == True and ADD4[1] == True and ADD4[2] == True:
            print("Player won!")
            End = 1
            penup()
            right(45)
            width(5)
            forward(300*sqrt(2)/24)
            pendown()
            forward(300*sqrt(2)/24*22)
            left(45)
            break
        elif ADD4[0] == False and ADD4[1] == False and ADD4[2] == False:
            print("PC won!")
            End = 1
            penup()
            right(45)
            width(5)
            forward(300*sqrt(2)/24)
            pendown()
            forward(300*sqrt(2)/24*22)
            left(45)
            break
        elif ADD5[0] == True and ADD5[1] == True and ADD5[2] == True:
            print("Player won!")
            End = 1
            width(5)
            penup()
            forward(300)
            right(180)
            left(45)
            forward(300*sqrt(2)/24)
            pendown()
            forward(300*sqrt(2)/24*22)
            right(45+180)
            break
        elif ADD5[0] == False and ADD5[1] == False and ADD5[2] == False:
            print("PC won!")
            End = 1
            width(5)
            penup()
            forward(300)
            right(180)
            left(45)
            forward(300*sqrt(2)/24)
            pendown()
            forward(300*sqrt(2)/24*22)
            right(45+180)
            break
    
#######################################################################################################################################################

        E = int(input('Your move: '))
        if E > 0 and E < 4:
            if L[0][E-1] == None:
                L[0][E-1] = True
                if E == 1:
                    penup()
                    goto(a1[0], a1[1])
                    down()
                    CROSS()
                elif E == 2:
                    penup()
                    goto(a2[0], a2[1])
                    down()
                    CROSS()
                elif E == 3:
                    penup()
                    goto(a3[0], a3[1])
                    down()
                    CROSS()
            else:
                print("Please, restart the program")
                exit()
        elif E > 3 and E < 7:
            if L[1][E-4] == None:
                L[1][E-4] = True
                if E == 4:
                    penup()
                    goto(a4[0], a4[1])
                    down()
                    CROSS()
                elif E == 5:
                    penup()
                    goto(a5[0], a5[1])
                    down()
                    CROSS()
                elif E == 6:
                    penup()
                    goto(a6[0], a6[1])
                    down()
                    CROSS()
            else:
                print("Please, restart the program")
                exit()
        elif E > 6 and E < 10:
            if L[2][E-7] == None:
                L[2][E-7] = True
                if E == 7:
                    penup()
                    goto(a7[0], a7[1])
                    down()
                    CROSS()
                elif E == 8:
                    penup()
                    goto(a8[0], a8[1])
                    down()
                    CROSS()
                elif E == 9:
                    penup()
                    goto(a9[0], a9[1])
                    down()
                    CROSS()
            else:
                print("Please, restart the program")
                exit()
        else:
            print("Please, restart the program")
            exit()

#######################################################################################################################################################

                                           #XNN
        ADD1 = [L[0][0], L[1][0], L[2][0]] #XNN
                                           #XNN
    
                                           #NXN
        ADD2 = [L[0][1], L[1][1], L[2][1]] #NXN
                                           #NXN
                                       
                                           #NNX
        ADD3 = [L[0][2], L[1][2], L[2][2]] #NNX
                                           #NNX
                                       
                                           #XNN
        ADD4 = [L[0][0], L[1][1], L[2][2]] #NXN
                                           #NNX
                                       
                                           #NNX
        ADD5 = [L[0][2], L[1][1], L[2][0]] #NXN
                                           #XNN

#######################################################################################################################################################

        if L[0][0] == True and L[0][1] == True and L[0][2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b1[0], b1[1])
            pendown()
            forward(250)
            break
        elif L[0][0] == False and L[0][1] == False and L[0][2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            goto(b1[0], b1[1])
            pendown()
            forward(250)
            break
        elif L[1][0] == True and L[1][1] == True and L[1][2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b2[0], b2[1])
            pendown()
            forward(250)
            break
        elif L[1][0] == False and L[1][1] == False and L[1][2] == False:
            print("PC won!")
            penup()
            width(5)
            goto(b2[0], b2[1])
            pendown()
            forward(250)
            break
        elif L[2][0] == True and L[2][1] == True and L[2][2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b3[0], b3[1])
            pendown()
            forward(250)
            break
        elif L[2][0] == False and L[2][1] == False and L[2][2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            goto(b3[0], b3[1])
            pendown()
            forward(250)
            break
        elif ADD1[0] == True and ADD1[1] == True and ADD1[2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b4[0], b4[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD1[0] == False and ADD1[1] == False and ADD1[2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            goto(b4[0], b4[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD2[0] == True and ADD2[1] == True and ADD2[2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b5[0], b5[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD2[0] == False and ADD2[1] == False and ADD2[2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            goto(b5[0], b5[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD3[0] == True and ADD3[1] == True and ADD3[2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            goto(b6[0], b6[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD3[0] == False and ADD3[1] == False and ADD3[2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            goto(b6[0], b6[1])
            right(90)
            pendown()
            forward(250)
            left(90)
            break
        elif ADD4[0] == True and ADD4[1] == True and ADD4[2] == True:
            print("Player won!")
            End = 1
            penup()
            width(5)
            right(45)
            forward(300*sqrt(2)/24)
            pendown()
            forward(300*sqrt(2)/24*22)
            left(45)
            break
        elif ADD4[0] == False and ADD4[1] == False and ADD4[2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            right(45)
            forward(300*sqrt(2)/24)
            pendown()
            forward(300*sqrt(2)/24*22)
            left(45)
            break
        elif ADD5[0] == True and ADD5[1] == True and ADD5[2] == True:
            print("Player won!")
            End = 1
            width(5)
            penup()
            forward(300)
            right(180)
            left(45)
            forward(300*sqrt(2)/24)
            pendown()
            forward(300*sqrt(2)/24*22)
            right(45+180)
            break
        elif ADD5[0] == False and ADD5[1] == False and ADD5[2] == False:
            print("PC won!")
            End = 1
            penup()
            width(5)
            forward(300)
            right(180)
            left(45)
            forward(300*sqrt(2)/24)
            pendown()
            forward(300*sqrt(2)/24*22)
            right(45+180)
            break
    if End == 0:
        print("Tie!")
    print("New game in 15 seconds.")
    sleep(15)
    clear()
    down()
