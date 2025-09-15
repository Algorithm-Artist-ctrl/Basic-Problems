'''Loan EMI Waiver
'''
def loan_emi_waiver(emi):
    if emi>= 12:
        print("Eligible for 1 EMI waiver.")
    else:
        print("Not eligible for EMI waiver.")
emis= int(input("Enter number of EMIs paid without delay: "))
loan_emi_waiver(emis)
