char= input("Enter a single character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
else:
    if char.isalpha():
        if char.lower() in 'aeiou':
            print("It is a vowel.")
        else:
            print("It is a consonant.")
    elif char.isdigit():
        print("It is a digit.")
    else:
        print("It is a special character.")
