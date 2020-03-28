def front_back(str):
    if len(str) > 0:
        first = str[0]
        last = str[len(str)-1]
        list1 = list(str)
        list1[0] = last
        list1[len(str)-1] = first
        val = "".join(list1)
        return val
    elif str == '':
        return ''


print(front_back(''))
print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
print(front_back("Tamara"))

# cleaner solution
# if len(str) <= 1:
#     return str

#   mid = str[1:len(str)-1]  # can be written as str[1:-1]

#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]
