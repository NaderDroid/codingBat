def make_out_word(out, word):
    val = out[0:2] + word + out[2:]
    return val


print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))
print(make_out_word("[[]]", "nader"))
