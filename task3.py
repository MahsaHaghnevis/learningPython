##
## task3
## created by Yseeva
## July 25
##

print("\tIN THIS PROGRAM I'LL CALCULATE IF YOU PASSED THIS SEMESTER ")

fname=input("--> Enter your firstname : ")
lname=input("--> Enter your familytname : ")
Fullname=fname+" "+lname
print("now enter your grades below: ")
s1=float(input(" == | "))
s2=float(input(" == | "))
s3=float(input(" == | "))

avg= (s1+s2+s3)/3

if avg>=17:
    print(f"Congrats! You passed with {avg} , {Fullname}")
elif avg<17 and avg>=12:
    print(f"Not bad! You passed with {avg} , {Fullname}")
else: 
    print(f"Sorry! You could not pass {Fullname} -> maybe next semester ")
