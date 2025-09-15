def scholarship_eligibility(marks, income):
    if marks >= 85 and income < 200000:
        print("Eligible for scholarship.")
    else:
        print("Not eligible for scholarship.")
marks = int(input("Enter your marks: "))
income =int(input("Enter your annual family income (₹): "))
scholarship_eligibility(marks, income)
