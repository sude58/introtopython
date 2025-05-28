my_list = [
    1,
    3,
    6,
    11,
    4,
    2,
    4,
    9,
    17,
    16,
    0,
]
parity_list = []
for number in my_list:
    if number % 2 == 0:
        parity_list.append("even")
    else:
        parity_list.append("odd")

print(parity_list)
