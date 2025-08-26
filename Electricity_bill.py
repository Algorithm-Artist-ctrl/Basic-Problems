unit=int(input("Enter Units:\n"))
if unit<=100:
    charge=unit*5
elif unit>100 and unit<=200:
    charge=unit*7
elif unit>200 and unit<=300:
    charge=unit*8.5
else:
    fixed_charge=(unit*10)+100
    charge=fixed_charge
print(charge)

