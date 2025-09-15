def System(Signal):
    if Signal=="red":
        return "Stop"
    elif Signal=="yellow":
        return "Get Ready"
    elif Signal=="green":
        return "Go"
    else:
        return "Invalid Signal"
sing=input("Enter A Signal:\n").strip().lower()
result=System(sing)
print(f"Traffic System ={result}")