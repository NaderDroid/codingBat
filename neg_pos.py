def pos_neg(a, b, negative):
    if negative:
        return (a < b and b < 0)
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)


print("The executeion is starting here")
print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
print(pos_neg(-4, -5, False))
print(pos_neg(-4, 5, False))
print(pos_neg(-4, 5, True), "this one")
print(pos_neg(1, 1, False))
print(pos_neg(-1, -1, False))
print(pos_neg(1, -1, True))
print(pos_neg(-1, 1, True))
print(pos_neg(1, 1, True))
print(pos_neg(-1, -1, True))
print(pos_neg(5, -5, False))
print(pos_neg(-6, 6, False))
print(pos_neg(-5, -6, False))
print(pos_neg(-2, -1, False))
print(pos_neg(1, 2, False))
print(pos_neg(-5, 6, True))
print(pos_neg(-5, -5, True))
print()
