def bmi_calculator(w,h):
    bmi = w/(h**2)#error
    print(f"BMI = {bmi}")
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
weight =float(input("Enter your weight in kg: "))
height =input(input("Enter your height in meters: "))
bmi_calculator(weight, height)
