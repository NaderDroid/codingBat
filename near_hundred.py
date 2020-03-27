def near_hundred(n):
    return True if (abs(n-100) <= 10) or (abs(n-200) <= 10) else False


print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
print(near_hundred(90))
print(near_hundred(190))
