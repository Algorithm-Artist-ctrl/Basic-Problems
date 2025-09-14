def grade_system(percentage):
    if percentage >= 95:
        print("Grade: A+")
        print("Distinction")
    elif percentage >= 90:
        print("Grade: A+")
    elif percentage >= 75:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 50:
        print("Grade: C")
    elif percentage >= 35:
        print("Grade: D")
    else:
        print("Grade: Fail")
percent = input(input("Enter your percentage: "))
grade_system(percent)
