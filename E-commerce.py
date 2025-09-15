'''
apply coupon only if order ≥2000 and coupon valid.
'''
def application(order,coupon=True):
    if order>=2000 and coupon == True:
        print("Coupon Valid")
    else:
        print("Not Valid")
ord=int(input("Enter Orden Price: "))
coupon=input("Enter Cuopon(True/False): ")
application(ord,coupon)