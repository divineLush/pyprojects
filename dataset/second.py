import pandas as pd

data = pd.read_csv('data.csv', dtype={'Unnamed: 0':str})

first_col = data[data.columns[0]]

ln = len(first_col[0])
rn = range(ln)

patient_names = data.iloc[0].index.values

indexes = []
for i in rn:
    for j in rn:
        if i > j:
            indexes.append((i, j))

global_res = pd.DataFrame()

first_res_col = []
for tuple in indexes:
    str_tuple_0 = str(tuple[0])
    str_tuple_1 = str(tuple[1])

    first_res_col.append('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '00')
    first_res_col.append('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '01')
    first_res_col.append('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '10')
    first_res_col.append('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '11')


global_res['variables'] = first_res_col


def calc_for_patient(i):
    patient_col = data[data.columns[i]]
    patient_name = patient_names[i]
    res = []

    for tuple in indexes:
        d00 = 0
        d01 = 0
        d10 = 0
        d11 = 0
        # print()
        # print(tuple)
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

        res.append(str(d00))
        res.append(str(d01))
        res.append(str(d10))
        res.append(str(d11))

        # print('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '00: ' + str(d00))
        # print('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '01: ' + str(d01))
        # print('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '10: ' + str(d10))
        # print('c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '11: ' + str(d11))

    global_res[patient_name] = res

        # res['c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '00'] = d00
        # res['c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '01'] = d01
        # res['c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '10'] = d10
        # res['c_' + str_tuple_0 + '_' + str_tuple_1 + '_' + '11'] = d11


for i in range(1, len(data.columns)):
    calc_for_patient(i)

global_res.to_csv('second_result.csv')
