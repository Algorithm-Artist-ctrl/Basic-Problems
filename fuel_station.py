def Fuel(ltr):
    if ltr>=20:
        rate=ltr*100
        dis=rate-(rate*0.05)
        print("Amount:",dis)
    else:
        print("Amount:",(ltr*100))
liter=float(input("Enter Petrol in litre: "))
Fuel(liter)