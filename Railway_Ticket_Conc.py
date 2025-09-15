tic = int(input("Enter Ticket Price:\n"))
age = int(input("Enter age:\n"))
gender = input("Enter gender (Male/Female):\n").strip().lower()
if age < 5:
    print("Ticket Price: Free")
elif age >= 60:
    price = tic * 0.5
    print("Ticket Price:", price)
elif gender == "female" and 18 <= age <= 59:
    price = tic * 0.75 
    print("Ticket Price:", price)
else:
    print("Ticket Price:", tic)
