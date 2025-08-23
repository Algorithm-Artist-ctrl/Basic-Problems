usr_input=input("Input a string:\n")
usr_string=[]
for j in usr_input:
    usr_string.append(j)
count=0
for i in usr_string:
    if i in "aeiouAEIOu":
        count=count+1
print("Occurance of vowels is",count)