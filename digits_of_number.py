num = int(input("Enter digit:\n"))
digits = []
while num > 0:
    digits.append(num % 10)
    num = num // 10
digits.reverse()
for digit in digits:
    print(digit, end=", ")
print()
