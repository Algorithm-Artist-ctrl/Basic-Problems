def quadratic_roots(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        print("Roots are real and distinct.")
    elif D == 0:
        print("Roots are real and equal.")
    else:
        print("Roots are imaginary (complex).")
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
if a == 0:
    print("Not a quadratic equation. 'a' must not be 0.")
else:
    quadratic_roots(a, b, c)
