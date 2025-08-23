usr_input=input("Enter number for list separetedd by spaces:\n")
usr_list=list(map(int,usr_input.split()))
max=0
for i in usr_list:
    if max<=i:
        max=i
print("Largest Number in a list is",max)

