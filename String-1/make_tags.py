def make_tags(tag, word):
    val = "<"+tag+">"+word+"</"+tag+">"
    return val


print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))
print(make_tags("p", "nader"))
