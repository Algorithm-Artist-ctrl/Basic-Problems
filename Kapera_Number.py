def is_kaprekar(n):
    sq = str(n ** 2)
    #print(sq)
    d = len(str(n))
    #print(int(sq[-d:]))
    #print(int(sq[:-d]))
    right = int(sq[-d:])
    left = int(sq[:-d]) 
    return left + right == n
print(is_kaprekar(45))