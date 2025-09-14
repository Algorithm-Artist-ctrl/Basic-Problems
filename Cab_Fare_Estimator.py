def cab_Fare(km,time):
    charge=float(input("Enter Per Km charge: "))
    if time<=10:
        return f"You have to pay",(charge*km)
    else:
        subcharge=float(input("Input Addition as you Drive in Night: " ))
        amt=(charge*km)+subcharge
        return f"You have to Pay {amt}"
km=12
time=7
print(cab_Fare(12,7))