'''Hotel Room Tariff Calculator
Room charges:

Deluxe → ₹2000/day
Super Deluxe → ₹3000/day
Suite → ₹5000/day
If stay > 5 days, give 10% discount.
'''
def hoteL_room(room, days):
    if room == "deluxe":
        bill = 2000 * days
        if days > 5:
            dis = bill * 0.10
            bill -= dis
        print("Room charges:\n", bill)
    elif room == "super deluxe":
        bill = 3000 * days
        if days > 5:
            dis = bill * 0.10
            bill -= dis
        print("Room charges:\n", bill)
    elif room == "suite":
        bill = 5000 * days
        if days > 5:
            dis = bill * 0.10
            bill -= dis
        print("Room charges:\n", bill)
    else:
        print("Please confirm your room type.")
print("Deluxe → ₹2000/day\nSuper Deluxe → ₹3000/day\nSuite → ₹5000/day")
room = input("Enter Room:\n").strip().lower()
days = int(input("Enter Days:\n"))
hoteL_room(room, days)
