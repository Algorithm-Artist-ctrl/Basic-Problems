def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x *= sign  
    
    reversed_num = int(str(x)[::-1])
    
    return sign * reversed_num
print(reverse(123))  
print(reverse(-123))  
print(reverse(120))   
