def valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Valid triangle.")
    else:
        print("Invalid triangle.")
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
valid_triangle(a, b, c)
