def hased(num):
    add=0
    temp=num
    while num>0:
        rem=num%10
        add=add+rem
        num=num//10
    if temp%add==0:
        print("Harshad Number")
    else:
        print("Not a Harshad Number")
digit=int(input("Enter number:\n"))
hased(digit)