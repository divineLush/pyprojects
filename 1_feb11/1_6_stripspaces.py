print('type some str pls')
inp = input()

res = inp

while(res[0] == ' ' or res[len(res) - 1] == ''):
    if (res[0] == ' '):
        res = res[1:]

    if (res[len(res) - 1] == ' '):
        res = res[:-1]

print(res)
