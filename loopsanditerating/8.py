# Dict comprehension
my_set = {
    "Fluffy",
    "Butterscotch",
    "Pudding",
    "Cheddar",
    "Cocoa",
}

my_dict = {element: len(element) for element in my_set if len(element) % 2 == 1}
print(my_dict)
