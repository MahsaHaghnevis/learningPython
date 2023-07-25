##
## task2
## created by Yseeva
## July 25
##
 
print("\t WELCOME TO TRIANGLE PROGRAM")
print("Instruction : \n |||| You enter 3 sides of your triangle then I'll tell wether you can make it or not ||| ")
side1=float(input("@@ Enter the first side : "))
side2=float(input("@@ Enter the second side : "))
side3=float(input("@@ Enter the third side : "))

max=max(side1,side2,side3)

if max==side1:
    if side2+side3>max :
        print("YES!")
    else :
        print("NO!")
elif max==side2:
    if side1+side3>max :
        print("YES!")
    else :
        print("NO!")
else:
    if side2+side1>max :
        print("YES!")
    else :
        print("NO!")
