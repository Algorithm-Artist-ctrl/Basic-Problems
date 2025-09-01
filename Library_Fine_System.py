class Library:
    day=7
    def __init__(self,days):
        self.days=days
    def calculate(self):
        if self.days<=7:
            return f" No fine "
        elif self.days>=8 and self.days<=14:
            charge=self.days-Library.day
            fine=charge*5
            return f"Your fine ${fine} as you return book after 7 days of period "
        elif self.days>=15 and self.days<=30:
            charge=self.days-Library.day
            fine=charge*10
            return f"You fine ${fine} as your return book after second week of period"
        else:
            return f"' Return Book' and your Membership is cancelled"
usr_input=int(input(" input days:   "))
l1=Library(usr_input)
print(l1.calculate())