from re import search
from StripSpaces_6 import stripstr

print('pls type first and last name')
inp = input()

res = stripstr(inp)
first = search(".*\s", res).group(0)[:-1]
last = search("\s.*", res).group(0)[1:]

print(f'{last} {first}')
