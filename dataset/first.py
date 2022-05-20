import csv

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = [(row[0], row[1]) for row in reader]
    data.pop(0)
    # print(data)

    ln = len(data[0][0])
    res = [0] * ln

    sum = 0
    for row in data:
        val = int(row[1])
        sum += val

        for i in range(ln):
            if row[0][i] == '1':
                res[i] += val


    res = [num / sum for num in res]

    with open('first_patient_output.txt', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        writer.writerow(list(range(1, 21)))
        writer.writerow(res)
