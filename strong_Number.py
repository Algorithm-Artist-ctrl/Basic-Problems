def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
def digit(n):
    temp=n
    sum=0
    while n>0:
        rem=n%10
        factorial=fact(rem)
        sum=sum+factorial
        #print(factorial)
        n=n//10
    if temp==sum:
        return f"It is strong Number"
    else:
        return f"it is not a strong number"
print(digit(145))
