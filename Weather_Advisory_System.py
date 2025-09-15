def system(temp, weather="hot"):
    if temp < 10 and weather == "raining":
        print("Carry umbrella & warm clothes")
    else:
        print("Normal")
temp = int(input("Enter Temperature in Celsius:\n"))
weather = input("Enter weather:\n").strip().lower()
system(temp, weather)
