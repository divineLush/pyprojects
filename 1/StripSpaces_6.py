def stripstr(str):
    res = str

    while(res[0] == ' ' or res[len(res) - 1] == ''):
        if (res[0] == ' '):
            res = res[1:]

        if (res[len(res) - 1] == ' '):
            res = res[:-1]

    return res


if __name__ == '__main__':
    print('type some str pls')
    inp = input()

    print(stripstr(inp))
