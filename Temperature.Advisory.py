'''Q20. Temperature Advisory
Input Celsius temperature:

< 0 → Freezing

0–20 → Cold

21–35 → Normal

36–45 → Hot
'''
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
