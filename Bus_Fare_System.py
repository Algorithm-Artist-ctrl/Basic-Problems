#   Let me know if you have better Option
class Bus:
    def __init__(self,age,ticket): 
        self.age=age 
        self.ticket=ticket
    def calculate_bill(self):
        if self.age <= 5:
            return f"Free Ticket"
        elif self.age > 5 and self.age <= 17:
            return f"Half Ticket Price is {self.ticket / 2}"
        elif self.age >= 18 and self.age <= 60:
            return f"Full Ticket Price is {self.ticket}"
        else:
           dis = 0.25 * self.ticket
           self.ticket = self.ticket - dis
           return f"25% discount on full ticket. Final Ticket price is {self.ticket}"
usr_age=int(input("Enter the age: ")) 
usr_ticket=int(input("Enter Ticket Price: ")) 
b1=Bus(usr_age,usr_ticket)
print(b1.calculate_bill())