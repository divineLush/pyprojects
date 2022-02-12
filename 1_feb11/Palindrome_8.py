from math import floor

print('type smth pls')
inp = input().lower()

is_palindrome = True
str = "".join(inp.split())
ln = len(str)
n = floor(ln / 2)

for i in range(n):
    if (str[i] != str[ln - i - 1]):
        is_palindrome = False
        break


if (is_palindrome):
    print('y')
else:
    print('n')
