inp = [1, 6, 3, 87, 2, 2, 4, 42, 6, 7, 10, 2, 7, 3, 3]

ln = len(inp)
sequences = []

for i in range(ln):
    seq = []
    for j in range(i, ln - 1):
        if (inp[j] <= inp[j + 1]):
            seq.append(inp[j])
        else:
            break

    if (len(seq) != 0):
        sequences.append(seq)


best = sequences[0]
for seq in sequences:
    if (len(seq) > len(best)):
        best = seq


print(best)
