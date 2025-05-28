my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
"""
1. Yes, two lists are equal since another_list will have same type and same value as my_list.
2. No, two lists will be in different memory space, so not same object.
3. Yes, two lists will be equal since they are same element of equal list.
4. Yes, two lists will be same object since list constructor will perform shallow copy and left nested collection as same object.
"""
