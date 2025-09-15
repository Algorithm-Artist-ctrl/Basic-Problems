def eligibile(age,weight):
    if age>=18 and weight >=50:
        print("Eligibile")
    else:
        print("Not Eligible")
age=int(input("Enter age:\n"))
weight=int(input("Enter Weight in kg: "))
eligibile(age,weight)