def hased(num):
    sum=0
    temp=num
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    if temp%sum==0:
        print("Harshad Number")
    else:
        print("Not a Harshad Number")
digit=int(input("Enter number:\n"))
hased(digit)