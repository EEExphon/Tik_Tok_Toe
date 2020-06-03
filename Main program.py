import SOL1
import SOL2
# MAIN PROGRAM:

yn = input("which way to play? 1 or 2")
sf = "y"
if yn == "1":
    while sf == "y":
        e1 = '1'
        e2 = '2'
        e3 = '3'
        e4 = '4'
        e5 = '5'
        e6 = '6'
        e7 = '7'
        e8 = '8'
        e9 = '9'
        SOL1.game (e1,e2,e3,e4,e5,e6,e7,e8,e9) #注意看这一步
        print(" "*30,"(Press ENTER to continue)")
        input("")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
else:
    while sf == "y":
        e = ['1','2','3'],['4','5','6'],['7','8','9']
        SOL2.game (e) #注意看这一步
        print(" "*30,"(Press ENTER to continue)")
        input("")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
