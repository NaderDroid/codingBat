def string_match(a, b):
    counter = 0
    for aa in range(len(a)):
        if aa < len(a)-1 and aa < len(b)-1:
            if a[aa] == b[aa] and b[aa+1] == a[aa+1]:
                counter += 1
    return counter


print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
print(string_match("nader", "nader"))
