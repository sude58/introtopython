def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()


my_dict = {
    "Karl": 108,
    "Clare": 175,
    "Karis": 140,
    "Trevor": 180,
    "Antonina": 132,
    "Chris": 101,
}

print(do_something(my_dict))
"""
Function will take the list of the dictionary and sort them in alphabetical order.
 Then select second key with the alphabetical order and return the capitalized key.
 Output will be printing CHRIS.
"""
