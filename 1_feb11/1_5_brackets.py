from math import floor

print('type some brackets pls')
inp = input()

ln = len(inp)

if (ln % 2 != 0):
    print('no')
else:
    is_correct = True
    n = int(ln / 2)

    brackets = [('(', ')'), ('{', '}'), ('[', ']')]

    for i in range(n):
        for br in brackets:
            first = inp[i] == br[0]
            last = inp[ln - i - 1] != br[1]

            if (first and last):
                is_correct = False
                break

#         if (inp[i] == '{' and inp[ln - i - 1] != '}'):
#             is_correct = False
#             break

    if (is_correct):
        print('ye')
    else:
        print('no')
