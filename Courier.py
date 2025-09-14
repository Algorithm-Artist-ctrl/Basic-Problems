def courier_charges(weight):
    if weight <= 1:
        print("Courier Charge: ₹50")
    elif weight <= 5:
        print("Courier Charge: ₹100")
    elif weight <= 10:
        print("Courier Charge: ₹200")
    else:
        print("Package not allowed (over 10 kg).")
weight =float(input("Enter package weight in kg: "))
courier_charges(weight)
