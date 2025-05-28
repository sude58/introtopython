print("johnson" in "Joe Johnson")  # False string comparison is case sensitive
print(
    "sen" not in "Joe Johnson"
)  # True while there are all characters present, there is no exact sequence of substring present
print(
    "Joe J" in "Joe Johnson"
)  # True there is exact sequence of substring present, index 0-4
print(5 in range(5))  # False, range does not include end
print(5 in range(6))  # True, range includes up to end - 1
print(5 not in range(5, 10))  # False, range includes start term, so 5 is in range
print(0 in range(10, 0, -1))  # False, end is not in range
print(4 in {6, 5, 4, 3, 2, 1})  # True, there is 4 in set
print({1, 2, 3} in {1, 2, 3})  # False, there is no set in the set
print(
    {3, 2} in {1, frozenset({2, 3})}
)  # True, set and frozenset are considered same type
