'''Q16. Mobile Recharge Plans'''
def plans(recharge,user):
    if user not in recharge:
        return "Invalid Plans"
    else:
        if user==199:
            return "28 days, 1.5GB/day"
        elif user==399:
            return "56 days, 2GB/day"
        else:
            return "84 days, 3GB/day"
print('''Recharge packs:
₹199
₹399 
₹599 
'''
)
recharge=[199,399,599]
user=int(input("input Recharge Pack:\n"))
print(plans(recharge,user))