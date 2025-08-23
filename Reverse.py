num=int(input("Enter digit: "))
digit=0
while(num>0):
    rem=num%10
    digit=digit*10+rem
    num=num//10
print(f"Reverse of the digit is {digit}")
