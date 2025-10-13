numbers = [1, 2, 2, 3, 4, 3, 2, 1, 5, 3]
frequency = {}
for i in range(len(numbers)):
    num = numbers[i]
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
for key in frequency:
    print(f"Number {key} appears {frequency[key]} times.")
