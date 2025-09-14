import string
user = input("Input Character:\n")
ch = string.ascii_letters
symbols = string.punctuation
if user in ch:
    if user in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")
elif user in symbols:
    print("Symbol")
elif user.isdigit():
    print("Digit")
else:
    print("Invalid input")
