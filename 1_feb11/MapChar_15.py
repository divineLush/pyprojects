print('type pls')
inp = input()

res = ''
for char in inp:
    if (char == '_'):
        res = res + '0'

    if (char == '|'):
        res = res + '1'


print(res)
