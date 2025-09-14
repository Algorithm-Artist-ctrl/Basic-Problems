'''Q17. Cinema Ticket Booking
Ticket cost:

Morning Show → ₹150

Evening Show → ₹200

Night Show → ₹250
If tickets ≥ 5, give 10% discount.
'''
def Cinema_Ticket_Booking(show,cost):
    if show == "morning show":
        bill = 150 * cost
        if cost >=5:
            dis = bill * 0.10
            bill -= dis
        print("Ticket Price:\n", bill)
    elif show == "evening show":
        bill = 200 * cost
        if cost >=5:
            dis = bill * 0.10
            bill -= dis
        print("Ticket Price:\n", bill)
    elif show == "night show":
        bill = 250 * cost
        if cost >=5:
            dis = bill * 0.10
            bill -= dis
        print("Ticket Price:\n", bill)
    else:
        print("Choose mention show")
print('''Morning Show → ₹150
Evening Show → ₹200
Night Show→ ₹250''')
show=input("Enter Show:\n").strip().lower()
cost=int(input("Enter No. of Tickets:\n"))
Cinema_Ticket_Booking(show,cost)
