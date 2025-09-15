def Marks_system(marks):
    if marks>= 95:
        print("Excellent")
    elif marks >=70 and marks<=89:
        print("Good")
    elif marks>=50 and marks<=69:
        print("Avegrage")
    elif marks<50:
        print("Poor")
    else:
        print("Fail")
marks= int(input("Enter your Makrs: "))
Marks_system(marks)
