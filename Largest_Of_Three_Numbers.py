num1=float(input("Enter First Number:\n"))
num2=float(input("Enter Second Number:\n"))
num3=float(input("Enter Third Number:\n"))
if num1>num2 and num1>num3:
    print("Largest Number is",num1)
elif num2>num1 and num2>num3:
    print("The largest Number is",num2)
elif num3>num1 and num3>num2:
    print("The Largest Number is",num3)
else:
    print("All three Numbers are equall")