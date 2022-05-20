import pandas as pd

data = pd.read_csv('data.csv', dtype={'Unnamed: 0':str})

first_col = data[data.columns[0]]

ln = len(first_col[0])
rn = range(ln)


indexes = []
for i in rn:
    for j in rn:
        if i != j:
            indexes.append((i, j))


def calc_for_patient(i):
    patient_col = data[data.columns[i]]

    for tuple in indexes:
        d00 = 0
        d01 = 0
        d10 = 0
        d11 = 0
        print()
        print(tuple)
        for j in range(len(first_col)):
            first = first_col[j][tuple[0]]
            second = first_col[j][tuple[1]]

            count = patient_col[j]

            if (first == '0' and second == '0'):
                d00 += count

            if (first == '0' and second == '1'):
                d01 += count

            if (first == '1' and second == '0'):
                d10 += count

            if (first == '1' and second == '1'):
                d11 += count


        sum = d00 + d01 + d10 + d11
        d00 /= sum
        d01 /= sum
        d10 /= sum
        d11 /= sum

        str_tuple_0 = str(tuple[0])
        str_tuple_1 = str(tuple[1])

        print('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '00: ' + str(d00))
        print('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '01: ' + str(d01))
        print('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '10: ' + str(d10))
        print('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '11: ' + str(d11))

        # res['c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '00'] = d00
        # res['c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '01'] = d01
        # res['c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '10'] = d10
        # res['c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '11'] = d11


patients_count = len(data.columns) - 1

# for i in range(1, patients_count):
#     calc_for_patient(i)
