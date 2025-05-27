def is_list_empty(my_list):
    if my_list:
        print("Not Empty")
    else:
        print("Empty")


is_list_empty([])
# It will output Empty since empty list is Falsy and will not trigger if statement.
