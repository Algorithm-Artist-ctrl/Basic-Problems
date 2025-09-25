user_input=input("Enter number separated by space:\n")
user_list = list(map(int, user_input.split()))
l=len(user_list)
for i in range(1,l):
    if i not in user_list:
        print("Msiing number",i)