def internet_speed_test(speed):
    if speed < 2:
        print("Speed Category: Slow")
    elif speed <= 10:
        print("Speed Category: Average")
    elif speed <= 50:
        print("Speed Category: Fast")
    else:
        print("Speed Category: Superfast")
speed = float(input("Enter your internet speed in Mbps: "))
internet_speed_test(speed)
