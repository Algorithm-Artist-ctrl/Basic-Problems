Total_amt=50000
debit=int(input("Enter amount to withdraw:\n"))
if Total_amt<debit:
    print("Insufficent Balance")
elif debit%100!=0:
    print("Invalid Amount")
else:
    withdraw=Total_amt-debit
    print("Remaining Balance",withdraw)