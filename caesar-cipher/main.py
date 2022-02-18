input = "Bpm acv eia apqvqvo wv bpm ami,"

key_low = "abcdefghijklmnopqrstuvwxyz"
key_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(n, txt):
    result = ""

    for char in txt:
        try:
            if char.isupper():
                index = key_upper.index(char)
                i =  (index - n) % 26
                result += key_upper[i]
            else:
                index = key_low.index(char)
                i =  (index - n) % 26
                result += key_low[i]
        except:
            result += char

    return result


def score(str):
    e = (str.count("e") + str.count("E")) * 0.13
    a = (str.count("a") + str.count("A")) * 0.82
    i = (str.count("i") + str.count("I")) * 0.7
    o = (str.count("o") + str.count("O")) * 0.75
    u = (str.count("u") + str.count("U")) * 0.28
    y = (str.count("y") + str.count("Y")) * 0.2

    return e + a + i + o + u + y


dec = [decrypt(i, input) for i in range(1, 26)]
dec_sorted = sorted(dec, key=lambda x: score(x), reverse=True)

for entry in dec_sorted:
    print(entry)
