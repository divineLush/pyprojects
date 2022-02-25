input_arr = [1, 5, 2, 7, 2]
input_arr.sort()

unique_arr = [input_arr[0]]
for i in range(1, len(input_arr)):
    if (input_arr[i] != input_arr[i-1]):
        unique_arr.append(input_arr[i])


print(unique_arr)

# res = []
# for el in unique_arr:
#     for el_1 in unique_arr:
#         if el <= el_1:
#             res.append((el, el_1))

res = [(el, el_1) for el in unique_arr for el_1 in unique_arr if el < el_1]

print(res)
