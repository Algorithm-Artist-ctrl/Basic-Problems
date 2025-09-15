def check_loan_eligibility(salary, cibil):
    if salary >= 25000 and cibil >= 700:
        print("Eligible for loan.")
    else:
        print("Not eligible for loan.")
s= float(input("Enter your monthly salary: "))
c = int(input("Enter your CIBIL score: "))
check_loan_eligibility(s, c)
