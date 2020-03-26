def diff21(n):
    # return (n-21)*-1 if n < 21 else (n-21)*n
    return abs(n-21) if n <= 21 else (abs(n-21))*2


print(diff21(19))
print(diff21(10))
print(diff21(21))
