def Atm(pin, correct):
    digit = 0
    temp = pin 
    while(temp > 0):
        digit = digit + 1
        temp = temp // 10
    if digit == 4:
        if pin == correct:
            return "Grant Acess"
        else:
            return "Incorrect"
    else:
        return "Invalid"
p = int(input("Enter ATM Pin:\n"))
right = 1234
result = Atm(p, right)
print(f"ATM PIN {result}")
