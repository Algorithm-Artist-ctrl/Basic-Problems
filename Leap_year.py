l = int(input("Enter Year:\n"))

if l % 4 == 0:
    if l % 100 == 0:
        if l % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
