str = "a a a b b c"
str_split = str.split()

res = {}

for word in str_split:
    if word in res:
        res[word] += 1
    else:
        res[word] = 1


print(str)
print(res)
