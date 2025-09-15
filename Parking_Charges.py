"Free for 2 hours, ₹20/hr (3–5 hrs), ₹50/hr (after 5 hrs)"
h=float(input("Hour:\n"))
if h<=2:
    print("Free")
elif h>2 and h<=3:
    charge=h*10
    print("Charges of Parking is ",charge)
elif h>3 and h<=5:
    charge=h*20
    print("Parking charge",charge)
else:
    charge=h*50
    print("Parking charge",charge)