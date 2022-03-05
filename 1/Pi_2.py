step = 1

th = 50 ** 2
k = 0
for i in range(-100, 100, step):
    for j in range (-100, 100, step):
        dist = i ** 2 + j ** 2
        if (dist <= th):
            k = k + 1

print(k / 10000 * 4)
