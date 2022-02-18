# input = [1, -2, 3, 1, 4, -3, 5, 2]
input = [8, -4, 5, 7, 3, -3, -2, 6]

min = input[0]
max = input[0]

for el in input:
    if el < min:
        min = el
    if el > max:
        max = el


dist = abs(max - min)

top = max if max >= 0 else 0
bottom = min if min <= 0 else 0

for row_num in range(top, bottom - 1, -1):
    str = ""
    for num in input:
        if (row_num >= 0):
            if (num >= row_num):
                str += "*"
            else:
                str += " "
        else:
            if (num <= row_num):
                str += "+"
            else:
                str += " "
    print(str)
