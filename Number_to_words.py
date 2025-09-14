dict={1:"one",2:"two",3:"Three",4:"four",5:"five",6:"six",7:"Seven",8:"eight",9:"nine"}
user=int(input("Enter number of day(1 to 7)\n"))
number=[1,2,3,4,5,6,7,8,9]
if user not in number:
    print("Try Again")
else:
    print(f"{dict[user]}")