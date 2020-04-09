def extra_end(str):
    val = str[len(str)-2:]*3
    return val


print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))
print(extra_end("nader"))
