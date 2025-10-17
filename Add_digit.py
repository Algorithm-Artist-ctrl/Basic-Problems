def digit_add(n):
    add = 0
    while n > 0:
        rem = n % 10
        add = add + rem
        n = n // 10
    print("Adding of digit is", add)
digit_add(123)