def online_shopping_delivery_charges(bill, is_prime):
    if bill >= 1000:
        return "Free Delivery"
    elif is_prime:
        return "Delivery Charge: ₹20 (Prime Member)"
    else:
        return "Delivery Charge: ₹50 (Non-Prime Member)"
print(online_shopping_delivery_charges(20000, True))   
print(online_shopping_delivery_charges(500, True))    
print(online_shopping_delivery_charges(500, False))  
