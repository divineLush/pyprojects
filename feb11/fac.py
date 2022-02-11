n = int(input())

if n == 0:
    print(1)
else:
    fac = 1
    for i in range(1, n):
        fac = fac * i
    print(fac)
