##
## task1
## created by Yseeva
## July 25
##

import math

print("\tWELCOME TO CALCULATOR PROGRAM")
print("* First enter what you wanna do : \n --> 1) + \t --> 2) - \t --> 3) / \t --> 4) * ")
print(" --> 5) sin \t --> 6) cos \t --> 7) tan \t --> 8) cot")
print(" --> 9) factoriel \t --> 10)radical")
option=int(input())

if option == 1 or option==2 or option==3 or option==4:
    num1=float(input("enter first number : "))
    num2=float(input("enter second number : "))
    if option==1:
        print(num1+num2)
    elif option==2:
        print(num1-num2)
    elif option==3  :
        if num2!=0:
            print(num1/num2)
        else:
           print("The second number can't be zero!")
           exit()
    elif option==4 :
        print(num1*num2)
elif option == 5 or option==6 or option==7 or option==8 or option==9 or option==10 :
     num3=float(input("enter desired number : "))
     if option==5:
        print(math.sin(num3))
     elif option==6:
         print(math.cos(num3))
     elif option==7:
         print(math.tan(num3))
     elif option==8:
         if math.tan(num3)!=0:
          print(1/math.tan(num3))
         else:
          print("not valid!")
     elif option==9 or 10 :
         if num3>=0:
             if option==9:
              print(math.factorial(num3))
             else:
              print(math.sqrt(num3))
         else:
             print("it can't be generated")
else:
     print("invalid number eneterd!")
 

        
