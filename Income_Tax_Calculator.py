'''Up to ₹2,50,000 → No tax

₹2,50,001–₹5,00,000 → 5% on amount above ₹2,50,000

₹5,00,001–₹10,00,000 → 20% on amount above ₹5,00,000 + ₹12,500

Above ₹10,00,000 → 30% on amount above ₹10,00,000 + ₹1,12,500
'''
inc=int(input("Enter Income:    "))
if inc>250001 and inc<+50000:
    tax=inc*0.05
    print("Tax",tax)
elif inc>500001 and inc<1000000:
    tax=inc*0.20
    print("Tax",tax)
elif inc>1000000:
    tax=inc*0.3
    print("Tax",tax)
else:
    print("No Tax")