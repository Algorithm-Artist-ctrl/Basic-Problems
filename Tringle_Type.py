def type_triangle(a, b, c):
    if a ==b and b==c:
        print("Equaliateral triangle.")
    elif a==b or b==c or c==a:       
        print("Isosceles triangle.")
    else:
        print("Scalena Triangle:")
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
type_triangle(a, b, c)
