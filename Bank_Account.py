def account(type):
    if type == "Savings":
        print("Benefit: Earn interest on your balance.")
    elif type == "Current":
        print("Benefit: No transaction limits, ideal for businesses.")
    elif type == "Salary":
        print("Benefit: Zero minimum balance requirement.")
    else:
        print("Invalid account type.")
ac_type = input("Enter account type (Savings, Current, Salary): ").strip().capitalize()
account(ac_type)
