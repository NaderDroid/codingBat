def string_bits(str):
    val = ""
    i = 0
    while i < len(str):
        if i % 2 == 0:
            val = val+str[i]
        i += 1
    return val


print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))

print(string_bits("nader"))
