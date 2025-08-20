a=float(input("Enter Side a \n"))
b=float(input("Enter Side b \n"))
c=float(input("Enter Side c \n"))
if (a+b)>c and (b+c)>a and (a+c)>b :
    print("Valid Triangle")
else:
    print("Not Valid")