def find_integers(collection):
    integers = []
    for element in collection:
        if type(element) is int:
            integers.append(element)
    return integers


my_tuple = (1, "a", "1", 3, [7], 3.1415, -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)  # [1, 3, -4]
