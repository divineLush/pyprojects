import csv

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = [(row[0], row[1]) for row in reader]
    data.pop(0)
    print(data)

    ln = len(data[0][0])
    res = [0] * ln

    for row in data:
        for i in range(ln):
            if row[0][i] == '1':
                res[i] += int(row[1])


    with open('first_patient_output', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        writer.writerow(list(range(1, 21)))
        writer.writerow(res)
