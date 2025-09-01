class Shoping:
    def __init__(self,bill):
        self.bill=bill
    def calculate(self):
        if self.bill>=5000:
            dis=0.2*self.bill
            self.bill=self.bill-dis
            return f"Total Bill is {self.bill} after discount of 20%"
        elif (self.bill>=2000 and self.bill<5000):
            dis=0.1*self.bill
            self.bill=self.bill-dis
            return f"Total bill is {self.bill} after discount of 10%"
        else:
            return f" Total bill is {self.bill}"
usr_input=int(input("Enter Bill:    "))
s1=Shoping(usr_input)
print(s1.calculate())