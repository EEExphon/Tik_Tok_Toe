# DEFINITION RICHARD余世炅

def game (e):

    j = 20
    
    print("       ======================================================")
    print("       ||||Welcome to my Table Game! Player O goes first.||||")
    print("       ======================================================")

    print("\n")

    print(" "*j+"/--- --- ---\ "+"\n"+" "*j+f"| {e[0][0]} | {e[0][1]} | {e[0][2]} |"+"\n"+" "*j+"|-----------|"+"\n"+" "*j+f"| {e[1][0]} | {e[1][1]} | {e[1][2]} |"+"\n"+" "*j+"|-----------|"+"\n"+" "*j+f"| {e[2][0]} | {e[2][1]} | {e[2][2]} |"+"\n"+" "*j+"\--- --- ---/ ")

    win = False
    B = [ ]
    counter = 1
    
    while win != True:

        counter = counter + 1

        if counter % 2 == 0:
            P = "O"
            print("\n")
            print(" "*26+"----------------")
            print(" "*26+"Player O's turn.")
            print("------------------------------------------------------------------")
        else:
            P = "X"
            print("\n")
            print(" "*26+"----------------")
            print(" "*26+"Player X's turn.")
            print("------------------------------------------------------------------")
        
        print("which area do you want to enter? (Enter a number between 1 and 9.)")
        print("------------------------------------------------------------------")
        t = input("===")
        
        #--------------------------------------------------------------
        
        while t.isdigit() != True:
            print("--------------------------------------")
            print("Wrong! Enter a number between 1 and 9.")
            print("--------------------------------------")
            t = input("===")

        #--------------------------------------------------------------

        while float(t) > 9.0 or float(t) < 1.0:
            print("--------------------------------------")
            print("Wrong! Enter a number between 1 and 9.")
            print("--------------------------------------")
            t = input("===")
        print("\n")
        
        #--------------------------------------------------------------

        while t in B:
            print("        ----------------------------------------------")
            print("        This block has been taken. Choose another one!")
            print("------------------------------------------------------------------")
            print("which area do you want to enter? (Enter a number between 1 and 9.)")
            print("------------------------------------------------------------------")
            t = input("===")
        B.append(t)

        #--------------------------------------------------------------
            
        if t == "1":
            e[0][0] = P
        elif t == "2":
            e[0][1] = P
        elif t == "3":
            e[0][2] = P
        elif t == "4":
            e[1][0] = P
        elif t == "5":
            e[1][1] = P
        elif t == "6":
            e[1][2] = P
        elif t == "7":
            e[2][0] = P
        elif t == "8":
            e[2][1] = P
        elif t == "9":
            e[2][2] = P
        #--------------------------------------------------------------
        print(" "*j+"/--- --- ---\ "+"\n"+" "*j+f"| {e[0][0]} | {e[0][1]} | {e[0][2]} |"+"\n"+" "*j+"|-----------|"+"\n"+" "*j+f"| {e[1][0]} | {e[1][1]} | {e[1][2]} |"+"\n"+" "*j+"|-----------|"+"\n"+" "*j+f"| {e[2][0]} | {e[2][1]} | {e[2][2]} |"+"\n"+" "*j+"\--- --- ---/ ")
        print("\n")
        #--------------------------------------------------------------
        x = 0
        y = 0
        Q = [ ]
        W = [ ]
        #====================================================================================================
        for x in range (0,3):
            for y in range (0,3):
                Q.append(e[x][y])
            if Q[0] == Q[1] == Q[2]:
                if counter % 2 == 0:
                    print(" "*20+"@@@@@@@@@@@@@@@@@")
                    print(" "*20+"@ PLAYER O WINS @")
                    print(" "*20+"@@@@@@@@@@@@@@@@@")
                    Q = [ ]
                    win = True
                else:
                    print(" "*20+"@@@@@@@@@@@@@@@@@")
                    print(" "*20+"@ PLAYER X WINS @")
                    print(" "*20+"@@@@@@@@@@@@@@@@@")
                    Q = [ ]
                    win = True
            else:
                Q = [ ]
        #====================================================================================================        
        for y in range (0,3):
            for x in range (0,3):
                W.append(e[x][y])
            if W[0] == W[1] == W[2]:
                if counter % 2 == 0:
                    print(" "*20+"@@@@@@@@@@@@@@@@@")
                    print(" "*20+"@ PLAYER O WINS @")
                    print(" "*20+"@@@@@@@@@@@@@@@@@")
                    W = [ ]
                    win = True
                else:
                    print(" "*20+"@@@@@@@@@@@@@@@@@")
                    print(" "*20+"@ PLAYER X WINS @")
                    print(" "*20+"@@@@@@@@@@@@@@@@@")
                    W = [ ]
                    win = True
            else:
                W = [ ]
        #====================================================================================================        
        if e[0][0] == e[1][1] == e[2][2]:
            if counter % 2 == 0:
                print(" "*20+"@@@@@@@@@@@@@@@@@")
                print(" "*20+"@ PLAYER O WINS @")
                print(" "*20+"@@@@@@@@@@@@@@@@@")
            else:
                print(" "*20+"@@@@@@@@@@@@@@@@@")
                print(" "*20+"@ PLAYER X WINS @")
                print(" "*20+"@@@@@@@@@@@@@@@@@")
            win = True    
        elif e[0][2] == e[1][1] == e[2][0]:
            if counter % 2 == 0:
                print(" "*20+"@@@@@@@@@@@@@@@@@")
                print(" "*20+"@ PLAYER O WINS @")
                print(" "*20+"@@@@@@@@@@@@@@@@@")
            else:
                print(" "*20+"@@@@@@@@@@@@@@@@@")
                print(" "*20+"@ PLAYER X WINS @")
                print(" "*20+"@@@@@@@@@@@@@@@@@")
            win = True
        #====================================================================================================    
        if counter == 10 and win != True:
            print(" "*20+"@@@@@@@@@@@@@@@@@")
            print(" "*20+"@ D   R   A   W @")
            print(" "*20+"@@@@@@@@@@@@@@@@@")
            win = True

