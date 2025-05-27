def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)


foo()
# It will raise an error since there is no argument given for the first parameter and no default argument for that parameter exists.
