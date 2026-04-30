def temperature_system(temperature):
    if temperature>=45:
        print("Heat Wave Alert ")
    elif temperature >=36 and temperature<45:
        print("Hot")
    elif temperature>=21 and temperature <=35:
        print("Normal")
    elif temperature==0 and temperature <= 20:
        print("cold")
    else:
        print("Freezing")
temp = float(input("Input celsisu temperature: "))
temperature_system(temp)
