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


def calc_score(str):
    e = (str.count("e") + str.count("E")) * 0.13
    a = (str.count("a") + str.count("A")) * 0.82
    i = (str.count("i") + str.count("I")) * 0.7
    o = (str.count("o") + str.count("O")) * 0.75

    return e + a + i + o


def compare_results(a, b):
    a_score = calc_score(a)
    b_score = calc_score(b)

    if (a_score > b_score):
        return 1
    elif (a_score == b_score):
        return 0
    else:
        return -1


dec = [decrypt(i, input) for i in range(1, 26)]
dec_sorted = sorted(dec, key=lambda x: calc_score(x), reverse=True)

for entry in dec_sorted:
    print(entry)
