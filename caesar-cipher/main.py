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
    a = (str.count("a") + str.count("A")) * 0.082
    i = (str.count("i") + str.count("I")) * 0.07
    o = (str.count("o") + str.count("O")) * 0.075
    u = (str.count("u") + str.count("U")) * 0.028
    y = (str.count("y") + str.count("Y")) * 0.02

    return e + a + i + o + u + y


with open("test.txt") as input_file:
    first_line = input_file.readline()

    dec = [decrypt(i, first_line) for i in range(1, 26)]
    dec_sorted = sorted(dec, key=lambda x: score(x), reverse=True)

    print("\n\npls choose the right output:\n\n")

    for i in range(len(dec_sorted)):
        print(f"{i}. {dec_sorted[i]}")


    print("\n\n type smth from 0 to 24\n\n")
    user_num = int(input()) - 1

    with open("input.txt", "w") as output_file:
        for line in input_file:
            line_dec = decrypt(user_num, line)
            output_file.write(line_dec + "\n")
