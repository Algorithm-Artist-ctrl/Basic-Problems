class Password:
    def __init__(self,pasd):
        self.pasd=pasd
    def checker(self):
        strength=len(self.pasd)
        if strength<=6:
            return f" Weak Password "
        elif strength>6 and strength<=10:
            return f"Medium Strength Password "
        else:
            return f" Strong password "
usr_input=input("Enter password:    ")
p1=Password(usr_input)
print(p1.checker())