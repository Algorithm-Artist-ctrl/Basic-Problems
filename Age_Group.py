usr_age=int(input("Input Age:\n"))
if usr_age<13:
    print("Child")
elif usr_age>=13 and usr_age<=19:
    print("Teenage")
elif usr_age>=20 and usr_age<=59:
    print("Adult")
else:
    print("Senior")