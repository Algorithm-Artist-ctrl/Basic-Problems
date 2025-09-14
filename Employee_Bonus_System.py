salary=int(input("Enter Salary: "))
sev=int(input("Enter Experience year:   "))
if sev>10:
    bonus=salary*0.1
    print("Bonus:",bonus)
elif sev<10 and sev>6:
    bonus=salary*0.08
    print("Bonus",bonus)
elif  sev<6:
    bonus=salary*0.05
    print("Bonus",bonus) 
else:
    print("No Bonus")
  