def makes10(a, b):
    return True if (a == 10 or b == 10) or ((a+b) == 10) else False


print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))
print(makes10(-1, 11))
