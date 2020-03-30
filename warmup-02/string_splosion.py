def string_splosion(str):
    val = ""
    val1 = ""
    for i in str:
        val = val+i
        for j in val:
            val1 = val1+j
    return val1


print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))

print(string_splosion("nader"))

# sort of better solution
# =========
#  result = ""
#   # On each iteration, add the substring of the chars 0..i
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result
