# input_arr = [(1, 0), (2, 3), (4, 5)]
input_arr = [(3, 1), (0, 1), (-99, -100)]

clear_arr = [(el[1], el[0]) if el[1] < el[0] else el for el in input_arr]

print(clear_arr)

brackets = []
for el in clear_arr:
    brackets.append((el[0], False))
    brackets.append((el[1], True))


brackets.sort()
print(brackets)

res = 0
cur = 0
for el in brackets:
    if el[1]:
        cur -= 1
    else:
        cur += 1

    if cur > res:
        res = cur


print(cur)
print(res)
