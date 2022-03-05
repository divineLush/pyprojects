from math import sqrt


def is_prime(x):
    if (x <= 1):
        return False

    th = int(sqrt(x)) + 1
    for i in range(2, th):
        if (x % i == 0):
            return False

    return True


print('input smth pls')
inp = int(input()) + 1

for i in range(2, inp):
    if (is_prime(i)):
        print(i)
